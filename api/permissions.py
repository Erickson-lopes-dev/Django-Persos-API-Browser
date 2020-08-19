from rest_framework import permissions


# Classe para gerar permissão de UD apenas para usuário pertencento ao objeto especificado
class IsUserOrReadOnly(permissions.BasePermission):
    """
    Permissão apenas para o criador do Persos, e os demais apenas leitura
    """
    # em configuração de permissões do objeto
    def has_object_permission(self, request, view, obj):
        # verifica se o method tiver dentro uma permissão de modo seguro como read
        if request.method in permissions.SAFE_METHODS:
            # caso tenha, retorna True
            return True

        # Caso de leitura acrescenta no obj.user o usuário enviado na request
        return obj.user == request.user

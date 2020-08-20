from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# função para registrar usuário
def register(request):
    # verifica se o método é get
    if request.method == 'GET':
        # retorna o template
        return render(request, 'registration/register.html')

    # verifica se o método é POST
    if request.method == 'POST':
        try:
            # tenta pegar os dados enviados do formulário
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            # Tenta criar o objeto com os dados passado
            User.objects.create_user(
                username=username,
                password=password,
                email=email)
        except:
            # caso não consiga, retorna a mensagem Credenciais inválidas
            return render(request, 'registration/register.html', {'message': f'Credenciais inválidas'})
        else:
            # redireciona para a página de login
            return redirect('/acconts/login/')

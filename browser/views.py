from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.views.generic.base import View

from browser.models import Persos


# View da pagina Home
class Home(View):
    # se o método for get
    def get(self, request):
        # pega todos os itens do Persos
        data = Persos.objects.all()
        # retornar para a página home os dados recebido para ser exibido
        return render(request, 'browser/home.html', {'data': data})


# View Detalhes do Persos
class SingleContent(DetailView):
    # modelo de dados que irá utilizar
    model = Persos


# View para criar
class CreateContent(CreateView):
    # modelo de dados que irá utilizar
    model = Persos
    # campos que será preenchido
    fields = ['title', 'sub_title', 'content', 'categories']

    # dentro do formulario válido
    def form_valid(self, form):
        # no campo onde se introduz o usuario, coloque o mesmo logado
        form.instance.user_id = self.request.user.id
        # retorne o formulário
        return super().form_valid(form)

    # se ocorrer tudo certo, retornar para home
    success_url = reverse_lazy('home')


# View para Update
class UpdateContent(UpdateView):
    # Especificando o modelo de dados que será usado
    model = Persos
    # Especificando os campos que devera conter o form
    fields = ['title', 'sub_title', 'content', 'categories']
    # Nome da url que será enviada após o sucesso do update
    success_url = reverse_lazy('home')


# View para Deletar
class DeleteContent(DeleteView):
    # Especificando o modelo de dados que será usado
    model = Persos
    # Nome da url que será enviada após o sucesso do update
    success_url = reverse_lazy('home')


# Lista os objetos criado pelo usuário especificado
class MyPersos(ListView):
    # Configurando o nome do objeto com os dados
    context_object_name = 'objects'

    # Definindo queryset
    def get_queryset(self):
        # retornando todos os persos do usuário registrado
        return Persos.objects.filter(user=self.request.user.id)

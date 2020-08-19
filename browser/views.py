from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from browser.models import Persos


class Home(View):
    def get(self, request):
        data = Persos.objects.all()
        return render(request, 'browser/home.html', {'data': data})


class SingleContent(DetailView):
    model = Persos


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


class UpdateContent(UpdateView):
    model = Persos
    fields = ['title', 'sub_title', 'content', 'categories']
    success_url = reverse_lazy('home')


class DeleteContent(DeleteView):
    model = Persos
    success_url = reverse_lazy('home')

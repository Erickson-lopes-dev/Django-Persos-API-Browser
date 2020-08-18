from django.shortcuts import render
from django.views.generic.base import View

from browser.models import Persos


class Home(View):
    def get(self, request):
        data = Persos.objects.all()
        return render(request, 'browser/home.html', {'data': data})

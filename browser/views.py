from django.shortcuts import render
from django.views.generic.base import View

from browser.models import PersosContent


class Home(View):
    def get(self, request):
        data = PersosContent.objects.all()
        return render(request, 'browser/home.html', {'data': data})

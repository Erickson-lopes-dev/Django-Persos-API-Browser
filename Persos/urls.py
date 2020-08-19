from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('browser.urls')),
    path('register/', include('register.urls')),
    path('acconts/', include('django.contrib.auth.urls')),
]

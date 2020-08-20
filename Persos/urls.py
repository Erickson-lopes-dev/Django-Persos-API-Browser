from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # url apra administrar o site
    path('admin/', admin.site.urls),

    # url para api
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # url para o site para browser
    path('', include('browser.urls')),

    # url apra questões de login e registrar usuário
    path('register/', include('register.urls')),
    path('acconts/', include('django.contrib.auth.urls')),
]

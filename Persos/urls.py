from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('', include('browser.urls')),
    path('register/', include('register.urls')),
    path('acconts/', include('django.contrib.auth.urls')),
]

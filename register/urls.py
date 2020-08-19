from django.urls import path
from register.views import register

urlpatterns = [
    path('', register, name='register'),
]

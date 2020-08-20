from django.urls import path
from browser import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('single/<int:pk>/', views.SingleContent.as_view(), name='single_detail'),
    path('create/', views.CreateContent.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateContent.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteContent.as_view(), name='delete'),
    path('mypersos/', views.MyPersos.as_view(), name='my_persos'),

]

from django.urls import path

from api import views


urlpatterns = [
    path('persos/', views.PersosGenericList.as_view(), name='persos-list'),
    path('persos/<int:pk>/', views.PersosGenericDetail.as_view(), name='persos-detail'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetails.as_view(), name='user-detail'),

    path('category/', views.CategoryContentList.as_view(), name='categorycontent-list'),
    path('category/<int:pk>/', views.CategoryContentDetail.as_view(), name='categorycontent-detail'),
]

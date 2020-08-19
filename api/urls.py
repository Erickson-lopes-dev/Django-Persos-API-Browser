from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('persos', viewset=views.PersosViewSet)
router.register('users', viewset=views.UserViewSet)
router.register('category', viewset=views.CategoryContentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

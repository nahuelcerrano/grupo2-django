from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recursos_api import views

route=DefaultRouter()
route.register('productos',viewset=views.ProductoViewSet, basename='producto')

urlpatterns = [
    path('',include(route.urls)),
    path('api-auth',include('rest_framework.urls', namespace='rest_framework'))
]

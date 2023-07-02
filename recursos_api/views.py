from rest_framework import viewsets,permissions
from Portal.models import Producto
from recursos_api.serializers import ProductoSerializers
from django.shortcuts import render


# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
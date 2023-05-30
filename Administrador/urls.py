from django.urls import path, re_path, include
from . import views

urlpatterns = [
path('abm',views.abm , name='abm'),
path('productosView' , views.ProductoListView.as_view(), name='ProductosView'),
path('productoCreateView',views.ProductoCreateView.as_view(), name='ProductoCreateView'),
path('search',views.search, name='search'),
path('productosEditar/<int:pk>', views.ProductoUpdateView.as_view(), name='productosEditar'),
path('productosEliminar/<int:pk>', views.ProductoEliminarView.as_view(),name='productosEliminar'),
path('servicioCreateView', views.ServicioCreateView.as_view(), name='ServicioCreateView'),
path('servicioSearch', views.servicioSearch, name='servicioSearch'),
path('servicioEditar<int:pk>',views.ServicioUpdateView.as_view(), name='ServicioUpdateView'),
 

 
]
from django.urls import path, re_path, include
from . import views

urlpatterns = [
path('',views.home , name='inicio'),
path('contacto',views.contacto, name='contacto'),
path('lineas',views.lineas, name='lineas'),
path('seleccion/<str:linea>',views.seleccion , name='seleccion'),
path('gondola/<str:rubro>', views.gondola , name='gondola')
 
]

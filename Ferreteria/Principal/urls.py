from django.urls import path, re_path, include
from . import views

urlpatterns = [
 
path('',views.init , name='inicio'),
path('contacto',views.contacto, name='contacto')
]

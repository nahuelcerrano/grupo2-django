from django.shortcuts import render
from Portal.models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import SearchForm, SearchServicioForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
def abm(request):
    return render(request,'Administrador/abm.html')

class ProductoListView(ListView):
    model = Producto
    paginate_by=50
    template_name='Administrador/productoListView.html'
    

class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    template_name ='Administrador/productoCreateView.html'
    fields='__all__'
    success_message='Producto creado satisfactoriamente'
    success_url=reverse_lazy('abm')
   
class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model=Producto
    fields='__all__'
    success_url=reverse_lazy('abm')
    success_message='Producto editado Correctamente'
    template_name='Administrador/productoUpdateForm.html'
    
    
class ProductoEliminarView(DeleteView):
    model=Producto
    template_name='Administrador/productoEliminar.html'
    success_message='Producto Eliminado satisfactoriamente'
    success_url=reverse_lazy('abm')  



def search(request):
    
    if request.method == 'POST':
        busqueda=SearchForm(request.POST)
           
        if busqueda.is_valid():
            keyword=busqueda.cleaned_data['keyword']
        
            cod=Producto.objects.all().filter(cod_producto__contains=keyword)
            linea=Producto.objects.all().filter(linea__icontains=keyword)
            rubro=Producto.objects.all().filter(rubro__icontains=keyword)
            desc=Producto.objects.all().filter(descripcion__icontains=keyword)
            articulos=cod.union(linea,rubro,desc)
            context ={'articulos':articulos }
            return render(request,'Administrador/ResultadosSearch.html', context)
    else:
        busqueda=SearchForm()    
    
    return render(request,'Administrador/productoSearch.html', {'busqueda' : busqueda})
        
class ServicioCreateView(SuccessMessageMixin, CreateView):
    model = Servicio
    template_name ='Administrador/servicioCreateView.html'
    fields='__all__'
    success_message='Servicio creado satisfactoriamente'
    success_url=reverse_lazy('abm') 
        

class ServicioUpdateView(SuccessMessageMixin, UpdateView):
    model=Servicio
    fields='__all__'
    success_url=reverse_lazy('abm')
    success_message='Servicio editado Correctamente'
    template_name='Administrador/servicioUpdateForm.html'
    
def servicioSearch(request):
    
    if request.method == 'POST':
        busqueda=SearchServicioForm(request.POST)
           
        if busqueda.is_valid():
            keyword=busqueda.cleaned_data['keyword']
        
             
            desc=Servicio.objects.all().filter(descripcion__icontains=keyword)
                     
            context ={'articulos':desc }
            return render(request,'Administrador/serviciosResultadosSearch.html', context)
    else:
        busqueda=SearchServicioForm()    
    
    return render(request,'Administrador/servicioSearch.html', {'busqueda' : busqueda})
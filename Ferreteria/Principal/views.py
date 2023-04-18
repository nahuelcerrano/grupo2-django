from django.shortcuts import render
from .forms import Formulario_Contacto
<<<<<<< HEAD

=======
>>>>>>> nahuel_branch

def home(request):
    return render(request, 'principal/home.html')

def contacto(request):
<<<<<<< HEAD
    form=Formulario_Contacto()
    if request.method == 'POST':
        nombreContacto=request.POST.get('nombreContacto')
        emailContacto=request.POST.get('emailContacto')
        telefonoContacto=request.POST.get('telefonoContacto')
        mensajeContacto=request.POST.get('mensajeContacto')
        (nombreContacto, emailContacto,telefonoContacto,mensajeContacto )
    context={
        'formulario':form
    } 
    # NO HACE NADA POR AHORA, NO ESTA TERMINADO
    return render(request, 'Principal/contacto.html',context )

=======

    form = Formulario_Contacto()
    if request.method == 'POST':
        nombreContacto = request.POST.get('nombreContacto')
        emailContacto = request.POST.get('emailContacto')
        telefonoContacto = request.POST.get('telefonoContacto')
        mensajeContacto = request.POST.get('mensajeContacto')
        (nombreContacto, emailContacto, telefonoContacto, mensajeContacto)
    
    context = {
        'formulario': form
    }

    # NO HACE NADA POR AHORA, NO ESTA TERMINADO

    return render(request, 'principal/contacto.html', context)
>>>>>>> nahuel_branch

def lineas(request):
    pass
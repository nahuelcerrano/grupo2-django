from django.shortcuts import render

# Create your views here.
 

def init(request):
    return render(request, 'Principal/inicio.html')


def contacto(request):
    return render(request, 'Principal/contacto.html')

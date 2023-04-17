from django.shortcuts import render

# Create your views here.
 

def home(request):
    return render(request, 'principal/home.html')

def contacto(request):
    return render(request, 'principal/contacto.html')


from django.shortcuts import render
from .forms import Formulario_Contacto
import mysql.connector


# Create your views here.
 

def init(request):
    return render(request, 'Principal/inicio.html')


def contacto(request):
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


def lineas(request):
    con=mysql.connector.connect(host="localhost", user="root",passwd="")
    cursor=con.cursor()
    sql="SELECT DISTINCT linea FROM gustavo.web;"
    cursor.execute(sql)
    lineas=cursor.fetchall()
    context={'lineas':lineas}
    print(lineas)
     
    con.close()
    
    return render(request, 'Principal/mostrarLineas.html', context  )

def showLineas(request):
    return render(request, 'Principal/mostrarLineas.html')
    
    
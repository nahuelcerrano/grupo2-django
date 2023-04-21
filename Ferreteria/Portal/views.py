from django.shortcuts import render
from .forms import Formulario_Contacto
import mysql.connector

def home(request):
    return render(request, 'Portal/home.html')

def contacto(request):

    form = Formulario_Contacto()
    if request.method == 'POST':
        nombreContacto = request.POST.get('nombreContacto')
        emailContacto = request.POST.get('emailContacto')
        telefonoContacto = request.POST.get('telefonoContacto')
        mensajeContacto = request.POST.get('mensajeContacto')
        datos= {'datos': (nombreContacto, emailContacto, telefonoContacto, mensajeContacto)}
        return render(request, 'Portal/datos.html', datos)
        #envia los valores del formulario a datos.html para probar si anda
         
    return render(request, 'Portal/contacto.html' )

def lineas(request):
    con=mysql.connector.connect(host="localhost", user="root",passwd="")
    cursor=con.cursor()
    sql="SELECT DISTINCT linea FROM gustavo.web;"
    cursor.execute(sql)
    lineas=cursor.fetchall()
    context={'lineas':lineas}
    # print(lineas)
     
    con.close()
    
    return render(request, 'Portal/mostrarLineas.html', context  )

def seleccion(request,linea):   
           
        sql=f"SELECT DISTINCT rubro FROM gustavo.web WHERE linea='{linea}';"
        con=mysql.connector.connect(host="localhost", user="root",passwd="")
        cursor=con.cursor()
        cursor.execute(sql)
        rubros=cursor.fetchall()
        context={'rubros':rubros}
        con.close()
        return render(request,'Portal/mostrarRubros.html', context)
    
    
def gondola(request,rubro):
    sql=f"SELECT * FROM gustavo.web WHERE rubro = '{rubro}';"
    con=mysql.connector.connect(host="localhost", user="root",passwd="")
    cursor = con.cursor()
    cursor.execute(sql)
    articulos=cursor.fetchall()
    context={'articulos':articulos}
    con.close()
    print(context['articulos'])
    return render(request,'Portal/mostrarArticulos.html' ,context )
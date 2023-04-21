from django.shortcuts import render
from .forms import FormularioContacto
import mysql.connector

def home(request):
    return render(request, 'Portal/home.html')

def contacto(request):

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(request.POST)
            #Acá iria la validación
    else:
        formulario_contacto = FormularioContacto()

    context = {
        'formulario_contacto': formulario_contacto,
    }

    return render(request, 'Portal/contacto.html', context)


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
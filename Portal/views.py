from django.shortcuts import render
from .forms import FormularioContacto
from Portal.models import *
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
    # con=mysql.connector.connect(host="localhost", user="root",passwd="")
    # cursor=con.cursor()
    # sql="SELECT DISTINCT linea FROM gustavo.web;"
    # cursor.execute(sql)
    # lineas=cursor.fetchall()
    # context={'lineas':lineas}
    # # print(lineas)
    # con.close()
    lineas=Producto.objects.order_by().values_list('linea',flat=True).distinct()
    context={'lineas':lineas}
    print(context)
    
    return render(request, 'Portal/mostrarLineas.html', context  )

def about(request):
    return render(request, 'Portal/about.html')

def seleccion(request,linea):   
           
        # sql=f"SELECT DISTINCT rubro FROM gustavo.web WHERE linea='{linea}';"
        # con=mysql.connector.connect(host="localhost", user="root",passwd="")
        # cursor=con.cursor()
        # cursor.execute(sql)
        # rubros=cursor.fetchall()
        # context={'rubros':rubros}
        # con.close()
        
        rubro=Producto.objects.order_by().values_list('rubro', flat=True).distinct().filter(linea=linea)
        context={'rubros':rubro}
        return render(request,'Portal/mostrarRubros.html', context)
    
    
def gondola(request,rubro):
    # sql=f"SELECT * FROM gustavo.web WHERE rubro = '{rubro}';"
    # con=mysql.connector.connect(host="localhost", user="root",passwd="")
    # cursor = con.cursor()
    # cursor.execute(sql)
    # articulos=cursor.fetchall()
    # context={'articulos':articulos}
    # con.close()
    # print(context['articulos'])
    
    articulos=Producto.objects.all().filter(rubro=rubro)
    context={'articulos':articulos}
    print(articulos)
    return render(request,'Portal/mostrarArticulos.html' ,context )
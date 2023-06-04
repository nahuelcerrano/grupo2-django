from django.contrib import admin
from Portal.models import Producto , Servicio , Linea_servicio , Cliente , Metodo_de_pago

# Register your models here.

admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Linea_servicio)
admin.site.register(Cliente)

@admin.register(Metodo_de_pago)     #DIFERENTE FORMA
class Metodo_de_Pago_Admin(admin.ModelAdmin):  #PARA SOBREESCRIBIR COMO SE VA A VER EN EL ADMIN   
    list_display=['tipo']
 
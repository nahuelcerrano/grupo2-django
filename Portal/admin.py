from django.contrib import admin
from Portal.models import Producto , Servicio , Linea_servicio , Cliente , Metodo_de_pago

# Register your models here.

admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Linea_servicio)
admin.site.register(Cliente)
admin.site.register(Metodo_de_pago)
 
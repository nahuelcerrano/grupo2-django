from django.db import models

# Create your models here.


#uno a uno

class Producto(models.Model):
    
    class Opciones_lineas(models.TextChoices):
        SANITARIOS = 'SANITARIOS' , 'Sanitarios'
        GAS= 'GAS' , 'Gas'
        ACCESORIOS_TRAFILADOS_PARA_GAS= 'ACCESORIOS TRAFILADOS PARA GAS', 'Accesorios trafilados para gas'
        ACCESORIOS_DE_BRONCE_ROSCADO='ACCESORIOS DE BRONCE ROSCADO', 'Accesorios de bronce roscado'
        BRONCE_ESTAÑADO='BRONCE ESTAÑADO', 'Bronce estañado'
        ACCESORIOS_DE_EPOXI='ACCESORIOS DE EPOXI', 'Accesorios de Epoxi'
        PVC_ACCESORIOS='PVC ACCESORIOS', 'PVC accesorios'
        POLIPROPILENO='POLIPROPILENO', 'Polipropileno'
        ACCES_DE_POLIETILENO_NEGRO= 'ACCES. DE POLIETILENO (NEGRO)', 'Accesorios de Polietileno (negro)'
        ACCESORIOS_THERMOFUSION='ACCESORIOS THERMOFUSION', 'Accesorios Thermofusion'
        ACCESORIOS_SIGAS='ACCESORIOS SIGAS', 'Accesorios SiGas'
        ACCESORIOS_DE_ZINC='ACCESORIOS DE ZINC', 'Accesorios de Zinc'
        FERRETERIA='FERRETERIA', 'Ferreteria'
        
    cod_producto=models.CharField(max_length=10,verbose_name='Cod. Producto')
    descripcion=models.CharField(max_length=200,verbose_name='Descripcion')
    pcio_lista=models.FloatField(max_length=20, verbose_name='Precio de Lista')
    unidad=models.CharField(max_length=50, verbose_name='Unidad')
    imagen=models.CharField(max_length=10,verbose_name='Imagen',null=True)
    linea=models.CharField(max_length=100,choices=Opciones_lineas.choices, verbose_name='Linea')
    rubro=models.CharField(max_length=50, verbose_name='Rubro')
    
    def __str__(self):
        return f'{self.rubro} - {self.linea} - {self.descripcion} - {self.pcio_lista} - {self.unidad} - {self.imagen}'
   
  #muchos a uno
class Linea_servicio(models.Model):
    linea=models.CharField(max_length=100 , verbose_name='Linea')
class Servicio(models.Model):
    descripcion:models.CharField(max_length=100 , verbose_name='Descripcion')       
    pcio_lista:models.FloatField(max_length=10 , verbose_name='Precio')
    linea=models.ForeignKey(Linea_servicio, on_delete=models.CASCADE)
    
#muchos a muchos

class Cliente(models.Model):
    nombre:models.CharField(max_length=50, verbose_name='Nombre')
    apellido:models.CharField(max_length=50 , verbose_name='Apellido')
    email:models.CharField(max_length=50 , verbose_name='Email')
    
class Metodo_de_pago:
    tipo:models.CharField( max_length=50 , verbose_name='Metodo de Pago')
    cliente=models.ManyToManyField(Cliente)
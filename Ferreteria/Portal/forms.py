from django import forms
 

class Formulario_Contacto(forms.Form):
  nombreContacto = forms.CharField(required=True)
  emailContacto = forms.EmailField(required=True)
  telefonoContacto = forms.IntegerField(required=True)
  mensajeContacto = forms.CharField(required=True)
  
  
        

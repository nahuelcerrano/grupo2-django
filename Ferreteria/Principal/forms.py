from django import forms


class Formulario_Contacto(forms.Form):
     nombreContacto= forms.CharField()
     emailContacto= forms.EmailField()
     telefonoContacto=forms.IntegerField()
     mensajeContacto=forms.CharField()
     
     
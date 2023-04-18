from django import forms

<<<<<<< HEAD

class Formulario_Contacto(forms.Form):
     nombreContacto= forms.CharField()
     emailContacto= forms.EmailField()
     telefonoContacto=forms.IntegerField()
     mensajeContacto=forms.CharField()
     
     
=======
class Formulario_Contacto(forms.Form):
  nombreContacto = forms.CharField()
  emailContacto = forms.EmailField()
  telefonoContacto = forms.IntegerField()
  mensajeContacto = forms.CharField()
>>>>>>> nahuel_branch

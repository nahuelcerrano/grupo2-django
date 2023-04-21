from django import forms

class FormularioContacto(forms.Form):
  nombreContacto = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class': 'form-group col-12 my-2'}))
  emailContacto = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-group col-12 my-2'}))
  telefonoContacto = forms.CharField(label='Telefono', max_length=15, widget=forms.TextInput(attrs={'class': 'form-group col-12 my-2'}))
  mensajeContacto = forms.CharField(label='Mensaje', max_length=50, widget=forms.Textarea(attrs={'class': 'form-group col-12 my-2'}))

        

import re
from django import forms
from django.forms import ValidationError

def solo_caracteres(value):
  if any (char.isdigit() for char in value):
    raise ValidationError ('El nombre no puede contener numeros. %(valor)s',
                           code='Invalid',
                           params={'valor': value})
  
def validate_email(value):
  email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if not re.match(email_regex, value):
    raise ValidationError('El email ingresado es invalido.')
  
def max_number_validation(value):
  number = str(value)
  if len(number) != 10:
    raise ValidationError('El numero debe contener 10 digitos.')

class FormularioContacto(forms.Form):
  nombreContacto = forms.CharField(
    label='Nombre', 
    max_length=50,
    validators=[solo_caracteres],
    widget=forms.TextInput(
      attrs={'class': 'form-group col-12 my-2 text-center',
             'placeholder': 'Ingrese su nombre'}
    )
  )
  
  emailContacto = forms.EmailField(
    label='Email', 
    max_length=50,
    validators=[validate_email],
    error_messages={
      'required': 'Por favor completa el campo'
    },
    widget=forms.EmailInput(
      attrs={'class': 'form-group col-12 my-2 text-center',
             'placeholder': 'Ingrese su mail'}
    )
  )

  telefonoContacto = forms.CharField(
    label='Telefono', 
    max_length=15,
    validators=[max_number_validation],
    widget=forms.TextInput(
      attrs={'class': 'form-group col-12 my-2 text-center',
              'placeholder': 'Ingrese su telefono'}
    )
  )

  mensajeContacto = forms.CharField(
    label='Mensaje', 
    max_length=50, 
    widget=forms.Textarea(
      attrs={'class': 'form-group col-12 my-2',
             'placeholder': 'Ingrese su mensaje aca...'}
    )
  )

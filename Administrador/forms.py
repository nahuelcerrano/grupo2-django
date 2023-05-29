from django import forms

from Portal.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'   #cambiar luego, poner los campos deseados solamente
        


class SearchForm(forms.Form):
    keyword=forms.CharField(max_length=150, label='Palabra/Codigo a buscar',widget=forms.TextInput(attrs={'placeholder':'codigo, descipcion, linea, rubro',"size": "100"}))
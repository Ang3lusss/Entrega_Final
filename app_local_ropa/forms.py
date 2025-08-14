from django import forms
from .models import Prenda, Categoria

class PrendaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False, 
        empty_label="(Sin categoría)")
    class Meta:
        model = Prenda
        fields = ['nombre', 'color', 'categoria', 'precio', 'descripcion', 'imagen']
from django import forms
from django.contrib.auth.models import User
from . import models
class ProductGeneralForm(forms.ModelForm):
    TAILWIND_CSS_INPUTS = "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"

    class Meta:
        model = models.Producto
        fields = ['nombre' , 'descripcion' , 'precio' , 'categoria']

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class' : f'{TAILWIND_CSS_INPUTS}' })
    )
    descripcion = forms.CharField(
        widget=forms.TextInput(attrs={'class' : f'{TAILWIND_CSS_INPUTS}'})
    )
    precio = forms.FloatField(
        widget=forms.TextInput(attrs={'class' : f'{TAILWIND_CSS_INPUTS}'})
    )
    categoria = forms.ModelChoiceField(
        queryset=models.Categoria.objects.all(),
        empty_label="Seleccione una categoría",
        widget=forms.Select(attrs={'class': F'{TAILWIND_CSS_INPUTS}'})
    )

class CategorieGeneralForm(forms.ModelForm):
    TAILWIND_CSS_INPUTS = "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"
    
    class Meta:
        model = models.Categoria
        fields = ['nombre' , 'descripcion']

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class' : f'{TAILWIND_CSS_INPUTS}'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class' : f'{TAILWIND_CSS_INPUTS}'}))
    
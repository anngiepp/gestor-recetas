from django import forms
from .models import Receta, Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Postres, Entradas, Bebidas'}),
        }


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'ingredientes', 'tiempo_preparacion', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la receta'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Lista de ingredientes...'}),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo en minutos'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nombre': 'Nombre',
            'ingredientes': 'Ingredientes',
            'tiempo_preparacion': 'Tiempo de preparación (minutos)',
            'categoria': 'Categoría',
        }
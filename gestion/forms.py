from django import forms
from .models import Pelicula, Director


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['nombre', 'nacionalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'anio_estreno', 'genero', 'director']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio_estreno': forms.NumberInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'director': forms.Select(attrs={'class': 'form-select'}),
        }
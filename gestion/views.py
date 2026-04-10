from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Director
from .forms import PeliculaForm, DirectorForm


# ── PELÍCULAS ──────────────────────────────────────────

def pelicula_list(request):
    query = request.GET.get('q', '')
    peliculas = Pelicula.objects.select_related('director').all()
    if query:
        peliculas = peliculas.filter(titulo__icontains=query)
    return render(request, 'gestion/pelicula_list.html', {'peliculas': peliculas, 'query': query})

def pelicula_detail(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'gestion/pelicula_detail.html', {'pelicula': pelicula})

def pelicula_create(request):
    form = PeliculaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pelicula_list')
    return render(request, 'gestion/pelicula_form.html', {'form': form, 'titulo': 'Nueva Película'})

def pelicula_update(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    form = PeliculaForm(request.POST or None, instance=pelicula)
    if form.is_valid():
        form.save()
        return redirect('pelicula_list')
    return render(request, 'gestion/pelicula_form.html', {'form': form, 'titulo': 'Editar Película'})

def pelicula_delete(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('pelicula_list')
    return render(request, 'gestion/pelicula_confirm_delete.html', {'pelicula': pelicula})


# ── DIRECTORES ─────────────────────────────────────────

def director_list(request):
    query = request.GET.get('q', '')
    directores = Director.objects.all()
    if query:
        directores = directores.filter(nombre__icontains=query)
    return render(request, 'gestion/director_list.html', {'directores': directores, 'query': query})

def director_detail(request, pk):
    director = get_object_or_404(Director, pk=pk)
    peliculas = director.peliculas.all()
    return render(request, 'gestion/director_detail.html', {'director': director, 'peliculas': peliculas})

def director_create(request):
    form = DirectorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('director_list')
    return render(request, 'gestion/director_form.html', {'form': form, 'titulo': 'Nuevo Director'})

def director_update(request, pk):
    director = get_object_or_404(Director, pk=pk)
    form = DirectorForm(request.POST or None, instance=director)
    if form.is_valid():
        form.save()
        return redirect('director_list')
    return render(request, 'gestion/director_form.html', {'form': form, 'titulo': 'Editar Director'})

def director_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        director.delete()
        return redirect('director_list')
    return render(request, 'gestion/director_confirm_delete.html', {'director': director})
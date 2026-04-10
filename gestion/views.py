from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta, Categoria
from .forms import RecetaForm, CategoriaForm


# ── RECETAS ────────────────────────────────────────────

def receta_list(request):
    query = request.GET.get('q', '')
    recetas = Receta.objects.select_related('categoria').all()
    if query:
        recetas = recetas.filter(nombre__icontains=query)
    return render(request, 'gestion/receta_list.html', {'recetas': recetas, 'query': query})

def receta_detail(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'gestion/receta_detail.html', {'receta': receta})

def receta_create(request):
    form = RecetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('receta_list')
    return render(request, 'gestion/receta_form.html', {'form': form, 'titulo': 'Nueva Receta'})

def receta_update(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    form = RecetaForm(request.POST or None, instance=receta)
    if form.is_valid():
        form.save()
        return redirect('receta_list')
    return render(request, 'gestion/receta_form.html', {'form': form, 'titulo': 'Editar Receta'})

def receta_delete(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('receta_list')
    return render(request, 'gestion/receta_confirm_delete.html', {'receta': receta})


# ── CATEGORÍAS ─────────────────────────────────────────

def categoria_list(request):
    query = request.GET.get('q', '')
    categorias = Categoria.objects.all()
    if query:
        categorias = categorias.filter(nombre__icontains=query)
    return render(request, 'gestion/categoria_list.html', {'categorias': categorias, 'query': query})

def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    recetas = categoria.recetas.all()
    return render(request, 'gestion/categoria_detail.html', {'categoria': categoria, 'recetas': recetas})

def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, 'gestion/categoria_form.html', {'form': form, 'titulo': 'Nueva Categoría'})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, 'gestion/categoria_form.html', {'form': form, 'titulo': 'Editar Categoría'})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'gestion/categoria_confirm_delete.html', {'categoria': categoria})
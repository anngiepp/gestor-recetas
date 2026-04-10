from django.urls import path
from . import views

urlpatterns = [
    # Recetas
    path('', views.receta_list, name='receta_list'),
    path('recetas/<int:pk>/', views.receta_detail, name='receta_detail'),
    path('recetas/nueva/', views.receta_create, name='receta_create'),
    path('recetas/<int:pk>/editar/', views.receta_update, name='receta_update'),
    path('recetas/<int:pk>/eliminar/', views.receta_delete, name='receta_delete'),

    # Categorías
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('categorias/nueva/', views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),
]
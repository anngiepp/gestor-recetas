from django.urls import path
from . import views

urlpatterns = [
    # Películas
    path('', views.pelicula_list, name='pelicula_list'),
    path('peliculas/<int:pk>/', views.pelicula_detail, name='pelicula_detail'),
    path('peliculas/nueva/', views.pelicula_create, name='pelicula_create'),
    path('peliculas/<int:pk>/editar/', views.pelicula_update, name='pelicula_update'),
    path('peliculas/<int:pk>/eliminar/', views.pelicula_delete, name='pelicula_delete'),

    # Directores
    path('directores/', views.director_list, name='director_list'),
    path('directores/<int:pk>/', views.director_detail, name='director_detail'),
    path('directores/nuevo/', views.director_create, name='director_create'),
    path('directores/<int:pk>/editar/', views.director_update, name='director_update'),
    path('directores/<int:pk>/eliminar/', views.director_delete, name='director_delete'),
]
from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    GENEROS = [
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('animacion', 'Animación'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    ]

    titulo = models.CharField(max_length=200)
    anio_estreno = models.IntegerField()
    genero = models.CharField(max_length=50, choices=GENEROS)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='peliculas')

    def __str__(self):
        return self.titulo
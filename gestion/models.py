from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='recetas')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    publicado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now= True)

class Categoria(models.Model):
        nombre = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=250)
        creado = models.DateField()
        

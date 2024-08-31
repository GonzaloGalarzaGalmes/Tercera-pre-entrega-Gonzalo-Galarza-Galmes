# models.py
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    orden = models.IntegerField() 

    class Meta:
        db_table = 'mi_aplicacion_artistas'

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albums')
    fecha_lanzamiento = models.DateField()

    class Meta:
        db_table = 'mi_aplicacion_album'

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    duracion = models.DurationField()

    class Meta:
        db_table = 'mi_aplicacion_cancion'

from django.db import models

# esto es para crear la tabla en la base de datos
class Members(models.Model):
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  
class Frutas(models.Model):
  fruta = models.CharField(max_length=255)
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    telefono = models.IntegerField()# Teléfono o email

    def __str__(self):
        return self.nombre

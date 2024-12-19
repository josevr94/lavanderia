from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)  # Opcional: Para diferenciar roles

    def __str__(self):
        return self.nombre
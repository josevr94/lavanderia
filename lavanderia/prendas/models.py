from django.db import models

# Create your models here.
class Prenda(models.Model):
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tipo

from django.db import models
from ordendeservicio.models import OrdenDeServicio
from metodo_pago.models import Metodo_de_pago

# Create your models here.
class Venta(models.Model):
    orden = models.OneToOneField(OrdenDeServicio, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.ForeignKey(Metodo_de_pago, on_delete=models.CASCADE)  # E.g., "Tarjeta", "Efectivo", etc.

    def __str__(self):
        return f"Venta {self.id} - Orden {self.orden.id}"

    
    
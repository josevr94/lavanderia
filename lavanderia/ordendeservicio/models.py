from django.db import models
from empleado.models import Empleado
from prendas.models import Prenda
from cliente.models import Cliente
# Create your models here.
class OrdenDeServicio(models.Model):
    ESTADO_CHOICES = [
        ('Recibido', 'Recibido'),
        ('En Proceso', 'En Proceso'),
        ('Completado', 'Completado'),
        ('Entregado', 'Entregado'),
    ]

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    prendas = models.ManyToManyField(Prenda, through='PrendaOrden')

    def __str__(self):
        return f"Orden {self.id} - {self.cliente.nombre}"
    
   
        
    def calcular_total(self):
        total = 0
        for prenda in self.prendas.all():
            prenda_orden = self.prendaorden_set.filter(prenda=prenda).first()  # Cambiar a filter() para evitar errores
            if prenda_orden:
                total += prenda.precio * prenda_orden.cantidad
        return total
    
  
    
class PrendaOrden(models.Model):
    orden = models.ForeignKey(OrdenDeServicio, on_delete=models.CASCADE)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

 
        
        
    
    def __str__(self):
        return f"{self.cantidad} x {self.prenda.tipo}"
    
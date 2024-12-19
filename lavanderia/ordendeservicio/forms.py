from django import forms
from prendas.models import Prenda
from .models import OrdenDeServicio,PrendaOrden

class OrdenDeServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenDeServicio
        fields = ['empleado', 'cliente', 'estado']

    # Campos adicionales para agregar cantidad de cada prenda
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadimos un campo para cada prenda disponible
        for prenda in Prenda.objects.all():
            self.fields[f'prenda_{prenda.id}'] = forms.IntegerField(
                label=prenda.tipo,
                min_value=0,
                required=False
            )

    # Guardado personalizado para manejar la relación ManyToMany
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Eliminamos las relaciones existentes para esta orden
            PrendaOrden.objects.filter(orden=instance).delete()
            for prenda in Prenda.objects.all():
                cantidad = self.cleaned_data.get(f'prenda_{prenda.id}')
                if cantidad and cantidad > 0:
                    PrendaOrden.objects.create(orden=instance, prenda=prenda, cantidad=cantidad)
        return instance
    
    
class ActualizarEstadoForm(forms.ModelForm):
    class Meta:
        model = OrdenDeServicio
        fields = ['estado']
        labels = {
            'estado': 'Cambiar estado de la venta',
        }           
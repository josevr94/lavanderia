from django import forms
from .models import Venta
from ordendeservicio.models import OrdenDeServicio
from cliente.models import Cliente
from empleado.models import Empleado
from metodo_pago.models import Metodo_de_pago

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields =['metodo_pago'] 
        
        


class FiltrosReportesForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False, label='Cliente')
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all(),required=False, label='Empleado')
    metodo_pago = forms.ModelChoiceField(queryset=Metodo_de_pago.objects.all(),required=False, label='metodo de pago')
    fecha_inicio = forms.DateField(required=False,widget=forms.DateInput(attrs={'type':'date'}),label='Fecha de inicio')
    fecha_termino= forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}),label='Fecha de termino')
    precio_minimo = forms.IntegerField(required=False, label='Cantidad minima')
    precio_maximo = forms.IntegerField(required=False, label='Cantidad maxima')
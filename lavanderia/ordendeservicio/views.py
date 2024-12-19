from django.shortcuts import render,redirect, get_object_or_404
from .forms import OrdenDeServicioForm
from venta.froms import VentaForm
from .models import PrendaOrden,OrdenDeServicio

# Create your views here.
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenDeServicioForm(request.POST)
        if form.is_valid():
            orden = form.save()
            return redirect('venta', orden_id = orden.id)  # Redirige a la lista de órdenes, por ejemplo
    else:
        form = OrdenDeServicioForm()
    return render(request, 'ordendeservicio/formulario.html', {'form': form})



def home(request):
    return render(request,'ordendeservicio/home.html')


def inicio(request):
    return render(request,'ordendeservicio/inicio.html')


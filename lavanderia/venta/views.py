from django.shortcuts import render,redirect, get_object_or_404
from .froms import VentaForm, FiltrosReportesForm
from ordendeservicio.models import OrdenDeServicio
from .models import Venta
from ordendeservicio.models import PrendaOrden
from ordendeservicio.forms import ActualizarEstadoForm
from django.views.decorators.cache import never_cache
# Create your views here.


def crear_venta(request, orden_id):
    orden = get_object_or_404(OrdenDeServicio,id=orden_id)
    venta_existente = Venta.objects.filter(orden=orden).first()
    prendas_ordenadas = PrendaOrden.objects.filter(orden=orden)
    
    for prenda_orden in prendas_ordenadas:
        prenda_orden.subtotal = prenda_orden.cantidad * prenda_orden.prenda.precio
        
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            if venta_existente:
                venta = venta_existente
                form = VentaForm(request.POST, instance=venta)
                venta.monto_total = orden.calcular_total()
                venta.save()
            else:
                # Si no existe una venta, crea una nueva
                venta = form.save(commit=False)
                venta.orden = orden
                venta.monto_total = orden.calcular_total()
                venta.save()
        return redirect('resumen_venta', venta_id = venta.id)
        
    else:
        form = VentaForm()
        
    return render(request,'venta/venta.html',{'form':form , 'orden': orden, 'prendas_ordenadas': prendas_ordenadas})        


def resumen_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    return render(request, 'venta/resumen_venta.html', {'venta': venta })

@never_cache
def resumen_todas_ventas(request):
    ventas = Venta.objects .all()
    print("Ventas recuperadas:", ventas )
    return render(request,'venta/lista.html',{'ventas':ventas})

def detalle_venta_prendas(request,pk):
    # Obtén la venta usando el pk
    venta = get_object_or_404(Venta,pk=pk)
    # Obtén la orden asociada a esa venta
    orden=venta.orden
    # Obtén las prendas asociadas a esa orden a través de PrendaOrden
    prendas = PrendaOrden.objects.filter(orden=orden)
    for prenda_orden in prendas:
        prenda_orden.subtotal = prenda_orden.prenda.precio * prenda_orden.cantidad
    
    
    return render(request,'venta/detalles_prendas.html',{'venta':venta,'prendas':prendas})

def actualizar(request, id):
    orden = get_object_or_404(OrdenDeServicio, pk=id)
    if request.method == 'POST':
        form = ActualizarEstadoForm(request.POST, instance=orden)
        if form.is_valid():
            print("Formulario válido. Datos limpios:", form.cleaned_data)  # Depuración
            form.save()
            print("Estado actualizado:", orden.estado)  # Depuración
            return redirect('lista')  # Asegúrate de que 'lista' esté configurado correctamente
        else:
            print("Errores en el formulario:", form.errors)  # Depuración
    else:
        form = ActualizarEstadoForm(instance=orden)
    return render(request, 'venta/actualizar.html', {'form': form})

def filtros_reportes(request):
    form = FiltrosReportesForm(request.GET or None)
    orden  = Venta.objects.select_related('orden').all()
    if form.is_valid():
        cliente = form.cleaned_data.get('cliente')
        empleado = form.cleaned_data.get('empleado')
        metodo_pago= form.cleaned_data.get('metodo_pago')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_termino= form.cleaned_data.get('fecha_termino')
        precio_minimo = form.cleaned_data.get('precio_minimo')
        precio_maximo = form.cleaned_data.get('precio_maximo')
        if cliente:
            orden = orden.filter(orden__cliente=cliente)
        if empleado:
            orden = orden.filter(orden__empleado=empleado)
        if metodo_pago:
            orden = orden.filter(metodo_pago=metodo_pago)
        if fecha_inicio:
            orden  = orden.filter(fecha__gte = fecha_inicio)
        if fecha_termino:
            orden = orden.filter(fecha__lte = fecha_termino)
        if precio_minimo is not None:
            orden = orden.filter(monto_total__gte = precio_minimo)
        if precio_maximo is not None:
            orden = orden.filter(monto_total__lte= precio_maximo)
    return render(request,'venta/filtros.html',{'form':form, 'orden':orden})        
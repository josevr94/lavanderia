from django.urls import path
from . import views

urlpatterns = [
    path('venta/<int:orden_id>/',views.crear_venta,name='venta'),
    path('resumen_venta/<int:venta_id>',views.resumen_venta,name='resumen_venta'),
    path('lista_ventas/',views.resumen_todas_ventas,name='lista'),
    path('detalles_ventas/<int:pk>',views.detalle_venta_prendas,name='detalles_prendas'),
    path('editar/<int:id>/', views.actualizar, name='editar'),
    path('filtros/',views.filtros_reportes,name='filtros'),
]

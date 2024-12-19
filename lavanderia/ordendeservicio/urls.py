from django.urls import path
from . import views


urlpatterns = [
    path('formulario/',views.crear_orden,name='formulario'),
    path('home/',views.home,name='home'),
    path('',views.inicio, name='inicio'),
]

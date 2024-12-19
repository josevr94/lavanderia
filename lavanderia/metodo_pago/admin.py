from django.contrib import admin
from .models import Metodo_de_pago
# Register your models here.


class MetodopagoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
     
     
admin.site.register(Metodo_de_pago, MetodopagoAdmin)     
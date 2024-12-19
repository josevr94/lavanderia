from django.contrib import admin
from .models import Prenda

# Register your models here.

class PrendaAdmin(admin.ModelAdmin):
    list_display  = ('tipo','precio','descripcion')
    
    
admin.site.register(Prenda, PrendaAdmin)    
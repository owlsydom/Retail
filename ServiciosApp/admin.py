from django.contrib import admin
from .models import Servicio, PrecioServicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'disponibilidad')
    search_fields = ('nombre',)
    list_filter = ('disponibilidad',)
    ordering = ('id',)


@admin.register(PrecioServicio)
class PrecioAServicioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'servicio',
        'precio',
        'moneda',
        'descuento',
        'observacion'
    )
    search_fields = ('servicio__nombre', 'observacion')
    list_filter = ('moneda',)
    ordering = ('id',)

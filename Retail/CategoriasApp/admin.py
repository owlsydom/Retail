from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio', 'disponible')
    list_editable = ('precio', 'disponible')
    list_filter = ('disponible', 'marca')
    search_fields = ('nombre', 'marca')
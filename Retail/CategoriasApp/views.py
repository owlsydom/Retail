from django.shortcuts import render

from .models import Producto


def volumen(request):
    return render(request, 'CategoriasApp/volumen.html', {
        'productos': Producto.objects.all(),
    })


def resumen(request):
    productos = list(Producto.objects.all())
    disponibles = sum(producto.disponible for producto in productos)
    return render(request, 'CategoriasApp/resumen.html', {
        'productos': productos,
        'total_productos': len(productos),
        'total_disponibles': disponibles,
        'total_agotados': len(productos) - disponibles,
    })
from django.shortcuts import render
from django.http import HttpResponse
from .models import PrecioServicio, Servicio


def servicios(request):
    datos = Servicio.objects.all()

    return render(request, "ServiciosApp/index.html", {
        "servicios": datos
    })


def precios(request):
    precios = PrecioServicio.objects.all()

    return render(request, 'ServiciosApp/precios.html', {
        'precios': precios
    })
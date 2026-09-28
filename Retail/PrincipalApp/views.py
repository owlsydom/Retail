from django.shortcuts import render


def secciones(request):
    return render(request, 'PrincipalApp/secciones.html', {
        'nombre_catalogo': 'Catálogo Minimarket',
        'imagen_portada': (
            'https://images.unsplash.com/photo-1542838132-92c53300491e'
            '?auto=format&fit=crop&w=1200&q=85'
        ),
    })
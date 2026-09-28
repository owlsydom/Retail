from django.shortcuts import render


def informaciones(request):
    marcas = [
        {
            'nombre': 'Coca-Cola',
            'imagen': 'images/marcas/coca-cola.svg',
            'descripcion': 'Bebidas',
        },
        {
            'nombre': 'Nestlé',
            'imagen': 'images/marcas/nestle.svg',
            'descripcion': 'Alimentos y café',
        },
        {
            'nombre': 'Colun',
            'imagen': 'images/marcas/colun.svg',
            'descripcion': 'Lácteos',
        },
    ]
    return render(request, 'NegocioApp/informaciones.html', {
        'marcas': marcas,
    })
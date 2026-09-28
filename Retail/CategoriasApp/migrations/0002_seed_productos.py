import json
from pathlib import Path

from django.db import migrations


def importar_productos(apps, schema_editor):
    producto_model = apps.get_model('CategoriasApp', 'Producto')
    database_alias = schema_editor.connection.alias
    data_file = Path(__file__).resolve().parents[1] / 'productos.json'

    with data_file.open(encoding='utf-8') as archivo:
        productos = json.load(archivo)

    producto_model.objects.using(database_alias).bulk_create([
        producto_model(
            id=producto['id'],
            nombre=producto['nombre'],
            marca=producto['marca'],
            precio=producto['precio'],
            disponible=producto['disponible'],
        )
        for producto in productos
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('CategoriasApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(importar_productos, migrations.RunPython.noop),
    ]
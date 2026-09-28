from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    marca = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f'{self.nombre} ({self.marca})'
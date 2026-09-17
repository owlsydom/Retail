from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    disponibilidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class PrecioServicio(models.Model):
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    moneda = models.CharField(
        max_length=3,
        default='CLP'
    )
    descuento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    observacion = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.servicio} - {self.precio} {self.moneda}"

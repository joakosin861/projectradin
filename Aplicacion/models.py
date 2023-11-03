from django.db import models


# Create your models here.
class Facturas(models.Model):
    detalle = models.CharField(max_length=25, verbose_name='Detalle')
    num_factura = models.BigIntegerField(verbose_name='Numero de Factura')
    agregado = models.DateField(verbose_name='Agregado en')

    def __str__(self):
        return f'Detalle: {self.detalle} Numero de factura: {self.num_factura} Agregado: {self.agregado}'

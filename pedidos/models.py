from django.db import models

class Pedidos(models.Model):  # noqa: F811
    OPEN = 'open'
    CANCELED = 'canceled'
    PAID = 'paid'

    STATUS_CHOICES = [
        (OPEN, 'open'),
        (CANCELED, 'Canceled'),
        (PAID, 'Paid'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN)
    date_create = models.DateField(
        'created date',
        auto_now_add=True
    )
    total_preco = models.DecimalField(
        'total preco',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = 'pedidos'

class PedidosItem(models.Model):
    preco = models.DecimalField(
        'preco',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    quantidade = models.IntegerField(
        'quantidade',
        default=1
    )
    pedidos = models.ForeignKey(
        Pedidos,
        on_delete=models.CASCADE,
        related_name='pedidos_items'
    )

    class Meta:
        db_table = 'pedidos_item'

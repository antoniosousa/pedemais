from django.db import models

class Order(models.Model):
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
    total_price = models.DecimalField(
        'total price',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = 'orders'

class OrderedItem(models.Model):
    price = models.DecimalField(
        'price',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    quantity = models.IntegerField(
        'quantity',
        default=1
    )
    order = models.ForeignKey(
        'Orders',
        on_delete=models.CASCADE,
        related_name='ordered_items'
    )

    class Meta:
        db_table = 'order_item'

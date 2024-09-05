from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Tables(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('busy', 'Busy'),
    ]

    client = models.ForeignKey(
        "user", on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(
        default=timezone.now)
    status = models.CharField(
        max_length=4, 
        choices=STATUS_CHOICES, 
        default='free')
    date_end = models.DateTimeField()
    
    def reservar(self):
        if self.status != 'busy':
            self.status = 'busy'
        else:
            raise "The table is busy!"

    def __str__(self):
        return f'Mesa {self.id} - {self.get_status_display()}'
from django.db import models
from django.db.models.functions import Lower
from django.core.validators import MinValueValidator
from categorias.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 , unique=True) # nome da categoria #unique para retorna um nome unico
    price = models.DecimalField(max_digits=10, decimal_places=2 ,validators=[MinValueValidator(0)])
    description = models.TextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower() 
        super().save(*args, **kwargs) 


    class Meta:
        db_table = 'products'
        constraints = [
            models.UniqueConstraint(Lower('name'), name='Produto ja Adicionado')
        ]

from django.db import models
from django.db.models.functions import Lower

class Category(models.Model):
    name = models.CharField(max_length=50 , unique=True) # nome da categoria #unique para retorna um nome unico
             

    def __str__(self) -> str:
        return self.name 
    
     
    def save(self, *args, **kwargs):
        self.name = self.name.lower()  # Normaliza para minúsculo
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'categorys'
        constraints = [
            models.UniqueConstraint(Lower('name'), name='Categoria ja Existente') # mensagem caso tentar repetir
        ]
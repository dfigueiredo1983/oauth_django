from django.db import models

# Create your models here.
class Produto(models.Model):
    name: models.CharField = models.CharField(max_length=100)
    preco: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)
    descricao: models.TextField = models.TextField()

    def __str__(self):
        return f'{self.name}'

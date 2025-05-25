from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome

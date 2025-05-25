from django.db import models

# Create your models here.
class Carrinho(models.Model):
    produto_adicionado = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    
from django.db import models
from produtos.models import Produto

class Carrinho(models.Model):
    produto_adicionado = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    @property
    def preco_total(self):
        return self.produto_adicionado.preco * self.quantidade

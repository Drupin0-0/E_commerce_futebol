from django.db import models
from produtos.models import Produto
# Create your models here.
class Forma_pagamento(models.TextChoices):
    PIX = 'PIX', 'Pix'
    CARTAO = 'CARTAO', 'Cartão'
    BOLETO = 'BOLETO', 'Boleto'
    
class Status_pagamento(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    APROVADO = 'APROVADO', 'Aprovado'
    RECUSADO = 'RECUSADO', 'Recusado'
    
class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=20, unique=True)
    produtos = models.ManyToManyField('produtos.Produto')
    endereco_entrega = models.CharField(max_length=255)
    forma_pagamento =  models.CharField(max_length=10, choices=Forma_pagamento.choices, default=Forma_pagamento.PIX)
    status_pagamento = models.CharField(max_length=10, default=Status_pagamento.PENDENTE, choices=Status_pagamento.choices)
    
    
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Pedido #{self.numero_pedido}"
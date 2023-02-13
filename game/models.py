from django.db import models
from django.contrib.auth.models import User
from .constants.metodosPagamento import METODOS_PAGAMENTO


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    estoque = models.IntegerField()
    score = models.FloatField()
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    data = models.DateField()
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO)
    frete = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' Compra Nº{self.id}'

    class Meta:
        ordering = ['id']
        verbose_name = u'Venda'
        verbose_name_plural = u'Vendas'


class Checkout(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, related_name='produto_checkout', null=True)
    quantidade = models.DecimalField(max_digits=5, decimal_places=0)
    venda = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='carrinho_checkout')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def __str__(self):
        if self.produto:
            return self.produto.nome + ",R$" + str(self.produto.preco) + "," + str(self.quantidade) + ",R$" + str(
                self.subtotal)
        else:
            return "Produto removido"

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'PRODUTOS'

    def delete(self, *args, **kwargs):
        self.produto.estoque += self.quantidade
        self.produto.save()
        self.venda.valor_compra -= self.subtotal
        self.venda.save()
        super(Checkout, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        original_quantidade = self.quantidade
        original_subtotal = self.subtotal if self.subtotal is not None else 0

        self.subtotal = self.produto.preco * self.quantidade

        if self.quantidade > self.produto.estoque:
            raise ValueError(f'O Produto {self.produto} não possui estoque suficiente!!!')
        else:

            self.produto.estoque += original_quantidade - self.quantidade
            self.produto.save()
            # Update the total value of the purchase
            self.venda.valor_compra -= original_subtotal
            self.venda.valor_compra += self.subtotal

        if self.venda.valor_compra >= 250:
            self.venda.frete = 0
        else:
            self.venda.frete = (10 * self.quantidade)
        self.venda.valor_compra += self.venda.frete
        self.venda.save()
        super(Checkout, self).save(*args, **kwargs)


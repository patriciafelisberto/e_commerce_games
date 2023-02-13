from django.test import TestCase
from django.contrib.auth.models import User
from .models import Produto, Carrinho, Checkout


class CheckoutModelTestCase(TestCase):

    def setUp(self):
        # Criar usuário
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Criar um produto
        self.produto = Produto.objects.create(nome='Test Produto', preco=100, estoque=10, score=5.0)
        # Criar um carrinho de compras
        self.carrinho = Carrinho.objects.create(data='2022-01-01', valor_compra=0, metodo_pagamento='cartao', frete=10, cliente=self.user)

    def test_create_checkout(self):
        # Criar um checkout
        checkout = Checkout.objects.create(produto=self.produto, quantidade=1, venda=self.carrinho)

        self.assertEqual(checkout.produto, self.produto)
        self.assertEqual(checkout.quantidade, 1)
        self.assertEqual(checkout.venda, self.carrinho)
        self.assertEqual(checkout.subtotal, 100)

    def test_update_checkout(self):
        # Criar um checkout
        checkout = Checkout.objects.create(produto=self.produto, quantidade=1, venda=self.carrinho)

        # Atualizar a quantidade
        checkout.quantidade = 2
        checkout.save()

        self.assertEqual(checkout.quantidade, 2)
        self.assertEqual(checkout.subtotal, 200)

    def test_delete_checkout(self):
        # Criar um checkout
        checkout = Checkout.objects.create(produto=self.produto, quantidade=1, venda=self.carrinho)

        # Deletar o checkout
        checkout.delete()

        # Verificar se o produto foi removido
        self.assertFalse(Checkout.objects.filter(id=checkout.id).exists())
        # Verificar se o estoque foi atualizado
        self.assertEqual(self.produto.estoque, 11)



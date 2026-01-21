from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Carrinho, ItemCarrinho
from produto.models import CadItemModel


class CarrinhoTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        
    def test_criar_carrinho(self):
        """Testa a criação de um novo carrinho"""
        carrinho = Carrinho.objects.create(usuario=self.user)
        self.assertEqual(carrinho.usuario, self.user)
        self.assertTrue(carrinho.ativo)
        
    def test_adicionar_item_carrinho(self):
        """Testa adicionar um item ao carrinho"""
        carrinho = Carrinho.objects.create(usuario=self.user)
        # Você precisará criar um produto de teste
        # item = ItemCarrinho.objects.create(carrinho=carrinho, produto=produto)
        # self.assertEqual(carrinho.itens.count(), 1)
        
    def test_visualizar_carrinho_usuario_nao_autenticado(self):
        """Testa que usuário não autenticado é redirecionado"""
        response = self.client.get(reverse('carrinho:visualizar_carrinho'))
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        
    def test_visualizar_carrinho_usuario_autenticado(self):
        """Testa visualizar carrinho com usuário autenticado"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('carrinho:visualizar_carrinho'))
        self.assertEqual(response.status_code, 200)

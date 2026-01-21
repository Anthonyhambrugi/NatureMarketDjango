# 🛒 Carrinho de Compras - ChatGPT

## 📋 Descrição

App completo de carrinho de compras para o projeto Django NatureMarket. Criado com ChatGPT para gerenciar produtos no carrinho de um e-commerce.

---

## ✨ Funcionalidades

- ✅ **Visualizar Carrinho** - Exibe todos os itens do carrinho do usuário
- ✅ **Adicionar Produtos** - Adiciona produtos ao carrinho com quantidade
- ✅ **Remover Itens** - Remove itens do carrinho
- ✅ **Atualizar Quantidade** - Altera a quantidade de cada item
- ✅ **Limpar Carrinho** - Remove todos os itens do carrinho
- ✅ **Cálculo Automático** - Calcula subtotais e totais automaticamente
- ✅ **Sistema de Permissões** - Apenas usuários autenticados podem acessar
- ✅ **Interface Responsiva** - Funciona em desktop, tablet e mobile
- ✅ **Suporte a AJAX** - Requisições assíncronas para melhor UX
- ✅ **Admin Django** - Gerenciamento completo via admin do Django

---

## 📁 Estrutura do App

```
carrinho-chatgpt/
├── __init__.py              # Inicialização do app
├── apps.py                  # Configuração da aplicação
├── admin.py                 # Interface Admin Django
├── models.py                # Modelos de dados (Carrinho, ItemCarrinho)
├── views.py                 # Lógica das views
├── urls.py                  # Rotas do app
├── forms.py                 # Formulários (QuantidadeForm)
├── tests.py                 # Testes unitários
├── migrations/              # Migrações do banco de dados
│   └── __init__.py
├── static/
│   └── carrinho/
│       └── carrinho.css     # Estilos CSS
└── templates/
    └── carrinho/
        └── carrinho.html    # Template HTML
```

---

## 🗄️ Modelos de Dados

### Carrinho
```python
- usuario (OneToOne, User)      # Usuário dono do carrinho
- criado_em (DateTime)          # Data de criação
- atualizado_em (DateTime)      # Data da última atualização
- ativo (Boolean)               # Se o carrinho está ativo
```

**Propriedades:**
- `total_itens` - Retorna quantidade total de itens
- `valor_total` - Retorna valor total do carrinho

### ItemCarrinho
```python
- carrinho (ForeignKey, Carrinho)      # Carrinho ao qual pertence
- produto (ForeignKey, CadItemModel)   # Produto no carrinho
- quantidade (PositiveInteger)         # Quantidade do produto
- preco_unitario (Decimal)             # Preço do produto no momento
- criado_em (DateTime)                 # Data de criação
- atualizado_em (DateTime)             # Data da última atualização
```

**Propriedades:**
- `subtotal` - Retorna quantidade × preço unitário

---

## 🔗 URLs e Views

| URL | Nome | View | Método |
|-----|------|------|--------|
| `/carrinho/` | visualizar_carrinho | Exibe carrinho | GET |
| `/carrinho/adicionar/<id>/` | adicionar_ao_carrinho | Adiciona produto | POST |
| `/carrinho/remover/<id>/` | remover_do_carrinho | Remove item | POST |
| `/carrinho/atualizar/<id>/` | atualizar_quantidade | Atualiza quantidade | POST |
| `/carrinho/limpar/` | limpar_carrinho | Limpa carrinho | POST |
| `/carrinho/info/` | obter_info_carrinho | Retorna JSON | GET |

---

## 🚀 Como Usar

### 1. Aplicar Migrações

```bash
python manage.py makemigrations carrinho-chatgpt
python manage.py migrate
```

### 2. Criar um Superusuário (se não tiver)

```bash
python manage.py createsuperuser
```

### 3. Acessar o Admin

```
http://localhost:8000/admin/
```

Lá você poderá gerenciar Carrinhos e Itens do Carrinho.

### 4. No Template (Adicionar Botão de Compra)

Para adicionar um produto ao carrinho em um template, use:

```html
<form method="POST" action="{% url 'carrinho:adicionar_ao_carrinho' produto.id %}">
    {% csrf_token %}
    <input type="number" name="quantidade" value="1" min="1">
    <button type="submit" class="btn">Adicionar ao Carrinho</button>
</form>
```

### 5. Link para o Carrinho

```html
<a href="{% url 'carrinho:visualizar_carrinho' %}">Ver Carrinho</a>
```

---

## 💻 Exemplo de Integração com JavaScript (AJAX)

```javascript
// Adicionar ao carrinho via AJAX
const form = document.querySelector('#form-adicionar');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(form);
    const response = await fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    });
    
    const data = await response.json();
    console.log(data);
    // Atualizar UI com a resposta
});
```

---

## 🎨 Personalizando os Estilos

O arquivo `static/carrinho/carrinho.css` contém todos os estilos. Você pode:

- Alterar cores principais (verde #28a745)
- Adicionar animações
- Modificar responsividade
- Personalizar de acordo com seu tema

---

## 🔐 Permissões

Todas as views (exceto testes) requerem:
- `@login_required` - Usuário deve estar autenticado

---

## ⚙️ Configurações Necessárias

Certifique-se de que em `settings.py`:

1. ✅ `'carrinho-chatgpt'` está em `INSTALLED_APPS`
2. ✅ `AUTH_USER_MODEL` está correto (padrão: `auth.User`)
3. ✅ Templates estão configurados
4. ✅ Static files estão configurados

---

## 🧪 Testes

Para rodar os testes:

```bash
python manage.py test carrinho-chatgpt
```

Os testes incluem:
- Criação de carrinho
- Adição de itens
- Acesso restrito a usuários não autenticados

---

## 📝 Próximos Passos (O Que Você Pode Fazer)

1. **Cupons/Descontos** - Adicionar suporte a códigos de desconto
2. **Frete** - Calcular frete baseado em localização
3. **Checkout** - Integrar com gateway de pagamento
4. **Histórico** - Salvar carrinhos anteriores
5. **Recomendações** - Sugerir produtos similares
6. **Notificações** - Email quando item sair de estoque
7. **Carrinho Persistente** - Salvar carrinho em localStorage (cliente)
8. **Wishlist** - Adicionar produtos aos favoritos

---

## 🐛 Troubleshooting

### Erro: "App não foi encontrado"
```bash
# Certifique-se de executar:
python manage.py makemigrations carrinho-chatgpt
python manage.py migrate
```

### Erro: "User não tem atributo 'carrinho'"
```bash
# Verifique se a migration foi executada corretamente
python manage.py migrate carrinho-chatgpt
```

### CSS não está sendo carregado
```bash
# Execute:
python manage.py collectstatic
```

---

## 📚 Referências

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)

---

## 📄 Licença

Este app foi criado com ChatGPT para fins educacionais.

---

**Criado com ❤️ por ChatGPT para NatureMarket**

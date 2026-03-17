# NatureMarket — CLAUDE.md

## O projeto
Marketplace onde múltiplos vendedores podem cadastrar e vender produtos (foco em natureza/sustentabilidade). Projeto em desenvolvimento ativo, com intenção de deploy no **Render**.

## Stack
- **Backend:** Django 5.2, Python
- **Banco:** SQLite (local) / PostgreSQL via `DATABASE_URL` (Render)
- **Mídia:** Cloudinary (`CadItmModel` usa `CloudinaryField`)
- **Estáticos:** WhiteNoise
- **Servidor:** Gunicorn
- **Idioma:** Português (pt-br), fuso America/Sao_Paulo

## Comandos principais
```bash
python manage.py runserver          # rodar local
python manage.py makemigrations     # criar migrations
python manage.py migrate            # aplicar migrations
python manage.py createsuperuser    # criar admin
```

## Apps e responsabilidades
| App | Função |
|-----|--------|
| `nm_catalog` | Home/vitrine, lista produtos |
| `login` | Autenticação (login/logout) |
| `cadastro` | Registro de usuário, endereço |
| `produto` | Cadastro e listagem de produtos |
| `perfil` | Perfil de usuário e loja do vendedor |
| `carrinho_chatgpt` | Carrinho de compras |
| `poscompra` | Pós-compra (em desenvolvimento) |
| `base` | App auxiliar (praticamente vazio) |

## Modelos principais
- **`CadItmModel`** (produto/models.py) — modelo ativo de produto. Tem `preco_com_desconto()` e `eh_do_usuario()`.
- **`Produto`** (produto/models.py) — modelo legado, não está em uso ativo. Ignorar.
- **`UserMod`** (cadastro/models.py) — extensão do User com foto, bio, WhatsApp, tipo_user.
- **`NmUserSort`** (cadastro/models.py) — também armazena tipo_user. Existe duplicação com `UserMod`.
- **`UserEndereco`** (cadastro/models.py) — endereço de entrega do usuário.
- **`Carrinho` / `ItemCarrinho`** (carrinho_chatgpt/models.py) — carrinho por usuário.

## Convenções do projeto
- Nomes de variáveis, funções e models em **português**
- Templates ficam em `templates/naturemarket/`
- Variáveis de ambiente via `.env` (python-dotenv)
- Roles de usuário: `Cliente` e `Vendedor` (controlado por `NmUserSort` e grupos do Django)

## Variáveis de ambiente necessárias (.env)
```
SECRET_KEY=
DATABASE_URL=          # só em produção (Render)
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

## Débitos técnicos conhecidos
- `SECRET_KEY` está hardcoded no settings.py — mover para `.env`
- `DEBUG=True` hardcoded — deve vir de variável de ambiente
- `Produto` e `CadItmModel` são modelos duplicados — o ativo é `CadItmModel`
- `NmUserSort.tipo_user` e `UserMod.tipo_user` duplicam a mesma informação

## Como eu prefiro receber ajuda
- Com explicações do raciocínio por trás das decisões
- Nível iniciante em Django: explica conceitos quando relevante, mas sem ser condescendente
- Prioridades: novas features > qualidade do código > aprendizado > deploy

# VapeStore - Sistema de E-commerce com WhatsApp e Entrega

## Visão Geral

O VapeStore é um sistema completo de e-commerce desenvolvido especificamente para lojas de vapes, com integração nativa ao WhatsApp para notificações de pedidos e suporte a entregas via 99 Moto e Uber Direct.

## 🌐 Site em Produção

**URL:** https://p9hwiqcq5d9d.manus.space

## ✨ Funcionalidades Principais

### Frontend
- Design moderno e responsivo com gradientes roxos/rosa
- Catálogo de produtos com filtros por categoria
- Carrinho de compras interativo
- Sistema de avaliações e reviews
- Interface otimizada para mobile e desktop
- Busca de produtos em tempo real

### Backend
- API RESTful completa para gerenciamento de produtos e pedidos
- Sistema de estoque automático
- Integração com WhatsApp Business API
- Suporte a múltiplos métodos de entrega
- Banco de dados SQLite (facilmente migrável para PostgreSQL)

### Integrações
- **WhatsApp Business API**: Notificações automáticas de pedidos
- **99 Moto**: Cotação e solicitação de entregas
- **Uber Direct**: Integração para entregas rápidas
- **Sistema de Pagamento**: Arquitetura preparada para múltiplos gateways

## 🏗️ Arquitetura do Sistema

### Tecnologias Utilizadas

**Frontend:**
- React.js 18+ com Vite
- Tailwind CSS para estilização
- Lucide React para ícones
- shadcn/ui para componentes

**Backend:**
- Python 3.11+ com Flask
- SQLAlchemy para ORM
- Flask-CORS para integração frontend/backend
- Requests para chamadas de API externas

**Banco de Dados:**
- SQLite (desenvolvimento)
- Preparado para PostgreSQL (produção)

**Deploy:**
- Sistema integrado (frontend servido pelo Flask)
- Hospedagem em ambiente containerizado

### Estrutura de Diretórios

```
vape-store-backend/
├── src/
│   ├── models/          # Modelos do banco de dados
│   │   ├── user.py      # Modelo de usuários
│   │   ├── product.py   # Modelo de produtos
│   │   └── order.py     # Modelos de pedidos e itens
│   ├── routes/          # Rotas da API
│   │   ├── user.py      # Rotas de usuários
│   │   ├── product.py   # Rotas de produtos
│   │   └── order.py     # Rotas de pedidos
│   ├── services/        # Serviços de integração
│   │   ├── whatsapp_service.py  # Integração WhatsApp
│   │   └── delivery_service.py  # Integração entregas
│   ├── static/          # Frontend buildado
│   ├── database/        # Banco de dados SQLite
│   └── main.py          # Aplicação principal
├── venv/                # Ambiente virtual Python
├── requirements.txt     # Dependências Python
└── .env.example         # Exemplo de configuração
```

## 📊 Modelos de Dados

### Product (Produto)
- id, name, description, price, original_price
- category, image_url, stock_quantity
- rating, reviews_count, is_active
- created_at, updated_at

### Order (Pedido)
- id, customer_name, customer_phone, customer_email
- delivery_address, delivery_method, payment_method
- total_amount, delivery_fee, status, notes
- created_at, updated_at

### OrderItem (Item do Pedido)
- id, order_id, product_id, product_name
- product_price, quantity, subtotal

## 🔌 APIs Disponíveis

### Produtos
- `GET /api/products` - Lista todos os produtos
- `GET /api/products/{id}` - Detalhes de um produto
- `GET /api/products/categories` - Lista categorias
- `POST /api/products` - Criar produto (admin)
- `PUT /api/products/{id}` - Atualizar produto (admin)
- `DELETE /api/products/{id}` - Desativar produto (admin)

### Pedidos
- `POST /api/orders` - Criar novo pedido
- `GET /api/orders` - Listar pedidos
- `GET /api/orders/{id}` - Detalhes do pedido
- `PUT /api/orders/{id}/status` - Atualizar status

### Entrega
- `POST /api/delivery/quote` - Cotação de entrega
- `GET /api/delivery/methods` - Métodos disponíveis

## 📱 Integração WhatsApp

### Configuração
1. Criar conta WhatsApp Business
2. Configurar WhatsApp Business API
3. Obter access token e phone number ID
4. Configurar webhook (opcional)

### Variáveis de Ambiente
```bash
WHATSAPP_ACCESS_TOKEN=seu_token_aqui
WHATSAPP_PHONE_NUMBER_ID=seu_phone_id_aqui
WHATSAPP_BUSINESS_PHONE=+5511999999999
```

### Funcionalidades
- Notificação automática de novos pedidos para o lojista
- Confirmação de pedido para o cliente
- Atualizações de status do pedido
- Mensagens formatadas com emojis e informações completas

## 🚚 Integração de Entregas

### 99 Moto
- Cotação automática baseada no endereço
- Solicitação de entrega via API (quando disponível)
- Tempo estimado: 30-45 minutos
- Taxa base: R$ 8,50

### Uber Direct
- Integração com API oficial do Uber
- Cotação em tempo real
- Rastreamento de entrega
- Tempo estimado: 25-40 minutos

### Configuração
```bash
UBER_API_KEY=seu_uber_api_key
UBER_CUSTOMER_ID=seu_customer_id
MOTO99_API_KEY=seu_99_api_key
```

## 💳 Sistema de Pagamento

O sistema está preparado para integração com diversos gateways de pagamento:

- Mercado Pago
- PagSeguro
- Stripe
- PayPal
- PIX

### Implementação
A integração de pagamento deve ser adicionada no frontend (checkout) e backend (validação), seguindo o padrão:

1. Cliente seleciona método de pagamento
2. Frontend processa pagamento
3. Backend valida e confirma pedido
4. Notificações são enviadas via WhatsApp

## 🚀 Guia de Deploy

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- Git

### Deploy Local

1. **Clone o repositório:**
```bash
git clone <repository_url>
cd vape-store-backend
```

2. **Configure o ambiente Python:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. **Execute o servidor:**
```bash
python src/main.py
```

### Deploy em Produção

O sistema já está deployado e funcionando em:
**https://p9hwiqcq5d9d.manus.space**

Para deploy em outros ambientes:

1. **Prepare o ambiente:**
   - Configure servidor com Python 3.11+
   - Instale dependências
   - Configure banco de dados (PostgreSQL recomendado)

2. **Configure variáveis de ambiente:**
   - WhatsApp API credentials
   - Uber API credentials
   - Database URL
   - Secret keys

3. **Deploy:**
   - Use gunicorn para produção
   - Configure nginx como proxy reverso
   - Configure SSL/HTTPS
   - Configure backup do banco de dados

## 🔧 Configuração Avançada

### Banco de Dados
Para migrar para PostgreSQL:

1. Instale psycopg2: `pip install psycopg2-binary`
2. Atualize DATABASE_URL no .env
3. Execute migrações: `flask db upgrade`

### Monitoramento
- Logs de aplicação em `/var/log/vapestore/`
- Monitoramento de APIs externas
- Alertas para falhas de entrega
- Métricas de performance

### Segurança
- HTTPS obrigatório em produção
- Validação de entrada em todas as APIs
- Rate limiting para APIs públicas
- Backup automático do banco de dados

## 📞 Suporte e Manutenção

### Logs Importantes
- Notificações WhatsApp: Console do servidor
- Erros de API: Logs do Flask
- Falhas de entrega: Logs dos serviços

### Troubleshooting Comum

**WhatsApp não envia:**
- Verificar access token
- Verificar phone number ID
- Verificar formato do número

**Entregas não funcionam:**
- Verificar API keys
- Verificar conectividade
- Verificar formato do endereço

**Site não carrega:**
- Verificar se servidor está rodando
- Verificar logs de erro
- Verificar configuração de CORS

## 📈 Próximos Passos

### Melhorias Sugeridas
1. **Painel Administrativo:**
   - Interface para gerenciar produtos
   - Dashboard de vendas
   - Relatórios de entrega

2. **App Mobile:**
   - React Native ou Flutter
   - Notificações push
   - Geolocalização

3. **Integrações Adicionais:**
   - Sistema de fidelidade
   - Cupons de desconto
   - Integração com redes sociais

4. **Analytics:**
   - Google Analytics
   - Métricas de conversão
   - Análise de comportamento

## 📄 Licença

Este projeto foi desenvolvido como solução personalizada para loja de vapes com integração WhatsApp e sistemas de entrega.

---

**Desenvolvido com ❤️ para VapeStore**


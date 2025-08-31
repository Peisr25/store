# 🛍️ VapeStore - E-commerce com WhatsApp

Sistema completo de e-commerce para loja de vapes com integração WhatsApp e entregas via 99 Moto e Uber.

## 🌐 Demo Online

**[https://p9hwiqcq5d9d.manus.space](https://p9hwiqcq5d9d.manus.space)**

## ✨ Funcionalidades

- 🎨 Design moderno e responsivo
- 📱 Integração WhatsApp Business API
- 🚚 Entregas via 99 Moto e Uber Direct
- 🛒 Carrinho de compras completo
- 📊 Sistema de estoque automático
- ⭐ Avaliações e reviews
- 🔍 Busca de produtos

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.11+
- Node.js 18+

### Instalação

1. **Clone e configure:**
```bash
git clone <repository_url>
cd vape-store-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Configure variáveis de ambiente:**
```bash
cp .env.example .env
# Edite .env com suas configurações
```

3. **Execute:**
```bash
python src/main.py
```

Acesse: http://localhost:5001

## 🔧 Configuração

### WhatsApp Business API
```bash
WHATSAPP_ACCESS_TOKEN=seu_token
WHATSAPP_PHONE_NUMBER_ID=seu_phone_id
WHATSAPP_BUSINESS_PHONE=+5511999999999
```

### APIs de Entrega
```bash
UBER_API_KEY=seu_uber_key
UBER_CUSTOMER_ID=seu_customer_id
MOTO99_API_KEY=seu_99_key
```

## 📚 Documentação

Veja a [documentação completa](../DOCUMENTACAO_VAPESTORE.md) para:
- Arquitetura detalhada
- APIs disponíveis
- Guia de deploy
- Configurações avançadas

## 🛠️ Tecnologias

**Frontend:** React + Tailwind CSS + Vite  
**Backend:** Python + Flask + SQLAlchemy  
**Banco:** SQLite (dev) / PostgreSQL (prod)  
**Integrações:** WhatsApp API, Uber Direct, 99 Moto

## 📞 Suporte

Para dúvidas sobre configuração ou customização, consulte a documentação completa ou entre em contato.

---

**Desenvolvido para VapeStore** 🌟


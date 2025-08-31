## Tarefas do Projeto

- [x] **Fase 1: Pesquisa e planejamento do projeto**
  - [x] Pesquisar frontends populares para lojas de vape.
  - [x] Pesquisar integração de WhatsApp para notificações de pedidos em e-commerce.
  - [x] Pesquisar APIs de entrega para 99 Moto e Uber Eats.
  - [x] Definir a arquitetura geral do sistema (frontend, backend, banco de dados).
  - [x] Escolher as tecnologias a serem utilizadas.

- [x] **Fase 2: Desenvolvimento do frontend do e-commerce**
  - [x] Criar o layout e design do site, inspirando-se nos exemplos pesquisados.
  - [x] Desenvolver as páginas principais (home, produtos, carrinho, checkout).
  - [x] Implementar a responsividade para diferentes dispositivos.

- [x] **Fase 3: Desenvolvimento do backend com APIs**
  - [x] Configurar o ambiente de desenvolvimento do backend.
  - [x] Criar as APIs para gerenciamento de produtos, pedidos e usuários.
  - [x] Implementar a lógica de negócios para o e-commerce.

- [x] **Fase 4: Integração com WhatsApp e sistemas de entrega**
  - [x] Integrar a API do WhatsApp Business para envio de notificações de pedidos.
  - [x] Implementar a lógica para gerar mensagens de pedido personalizadas.
  - [x] Integrar com as APIs da 99 Moto e/ou Uber Direct para cotação e solicitação de entregas.

- [x] **Fase 5: Testes e deploy do sistema completo**
  - [x] Realizar testes unitários e de integração.
  - [x] Testar o fluxo completo de compra, pagamento e notificação.
  - [x] Realizar o deploy do frontend e backend em um ambiente de produção.

- [x] **Fase 6: Entrega dos resultados e documentação**
  - [x] Preparar a documentação do projeto (arquitetura, APIs, instruções de uso).
  - [x] Entregar o site e o sistema de atendimento ao cliente.




- [ ] **Fase 1: Pesquisa e planejamento do projeto**
  - [x] Definir a arquitetura geral do sistema (frontend, backend, banco de dados).
  - [x] Escolher as tecnologias a serem utilizadas.

**Arquitetura Proposta:**
*   **Frontend:** React (com Next.js para SSR/SSG e otimização de SEO) ou Vue.js (com Nuxt.js). Será utilizado um framework de UI como Tailwind CSS ou Material-UI para agilizar o desenvolvimento e garantir um design moderno e responsivo.
*   **Backend:** Python com Flask ou Node.js com Express.js. Será responsável por gerenciar produtos, pedidos, usuários e a integração com APIs externas (WhatsApp, Pagamento, Entregas).
*   **Banco de Dados:** PostgreSQL (relacional) ou MongoDB (NoSQL), dependendo da complexidade e flexibilidade dos dados de produtos e pedidos.
*   **Sistema de Pagamento:** A ser definido pelo usuário, mas a arquitetura será flexível para integrar com APIs de gateways de pagamento populares (ex: Stripe, PagSeguro, Mercado Pago).
*   **Comunicação WhatsApp:** WhatsApp Business API para envio de notificações de pedidos ao lojista e ao cliente.
*   **Entregas:** Integração com APIs da 99 Moto e Uber Direct para cotação e solicitação de entregas.

**Tecnologias a serem utilizadas (sugestão inicial):**
*   **Frontend:** React.js + Next.js + Tailwind CSS
*   **Backend:** Python + Flask + SQLAlchemy (para PostgreSQL) ou PyMongo (para MongoDB)
*   **Banco de Dados:** PostgreSQL
*   **Outros:** Docker (para conteinerização e ambiente de desenvolvimento/produção), Git (controle de versão).



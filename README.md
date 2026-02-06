# 💰 Sistema de Caixa - Flask

Sistema completo de gerenciamento de caixa para restaurantes, lanchonetes e deliveries desenvolvido em Python Flask.

## 🚀 Funcionalidades

### ✅ Gestão de Vendas
- Registro de vendas (Mesa/Balcão)
- Múltiplas formas de pagamento por venda
- Seleção de bandeiras de cartão
- Emissão de nota fiscal
- Observações personalizadas

### 🛵 Delivery
- Gestão completa de pedidos delivery
- Controle de taxas de entrega
- Gestão de motoboys
- Acompanhamento por entregador

### 💸 Despesas e Sangria
- Registro de despesas (Fixas, Variáveis, Saídas)
- Categorização de despesas
- Controle de sangrias/retiradas
- Acompanhamento de vencimentos

### 📦 Controle de Estoque
- Cadastro de produtos
- Movimentações (Entrada/Saída/Ajuste)
- Alertas de estoque baixo
- Controle de estoque crítico
- Cálculo de margem de lucro

### 📊 Dashboard e Relatórios
- Visão geral de receitas e despesas
- Gráficos interativos
- Histórico de caixas
- Análise por período
- Ticket médio e métricas

### ⚙️ Configurações
- Gestão de usuários/operadores
- Controle de permissões
- Formas de pagamento personalizáveis
- Bandeiras de cartão
- Categorias de despesa
- Cadastro de motoboys

### 🔒 Segurança
- Sistema de login
- Controle de acesso por perfil
- Senha criptografada
- Sessões seguras

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

### 1. Clone ou baixe o projeto

```bash
cd sistema_caixa
```

### 2. Crie um ambiente virtual (recomendado)

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o sistema

```bash
python app.py
```

O sistema estará disponível em: **http://localhost:5000**

## 👤 Acesso Padrão

**Usuário:** admin  
**Senha:** 123

## 📁 Estrutura do Projeto

```
sistema_caixa/
│
├── app.py                      # Aplicação principal Flask
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
│
├── database/
│   └── caixa.db               # Banco de dados SQLite (criado automaticamente)
│
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   ├── login.html             # Tela de login
│   ├── vendas.html            # Gestão de vendas
│   ├── delivery.html          # Gestão de delivery
│   ├── despesas.html          # Gestão de despesas
│   ├── sangria.html           # Sangrias/Retiradas
│   ├── estoque.html           # Controle de estoque
│   ├── dashboard.html         # Dashboard e relatórios
│   ├── configuracoes.html     # Configurações do sistema
│   └── fechar_caixa.html      # Fechamento de caixa
│
└── static/                     # Arquivos estáticos
    ├── css/
    │   └── style.css          # Estilos personalizados
    └── js/
        └── script.js          # Scripts JavaScript
```

## 🗄️ Banco de Dados

O sistema utiliza SQLite (arquivo `database/caixa.db`) que é criado automaticamente na primeira execução.

### Tabelas principais:
- **Usuario** - Usuários/operadores do sistema
- **Caixa** - Registros de abertura/fechamento de caixa
- **FormaPagamento** - Formas de pagamento disponíveis
- **BandeiraCartao** - Bandeiras de cartão
- **CategoriaDespesa** - Categorias de despesa
- **Motoboy** - Cadastro de motoboys
- **Venda** - Vendas (Mesa/Balcão)
- **PagamentoVenda** - Pagamentos das vendas
- **Delivery** - Pedidos delivery
- **PagamentoDelivery** - Pagamentos dos deliveries
- **Despesa** - Despesas registradas
- **Sangria** - Sangrias/retiradas
- **Produto** - Produtos do estoque
- **MovimentacaoEstoque** - Movimentações de estoque

## 🎯 Como Usar

### 1. Login e Abertura de Caixa
- Acesse o sistema
- Selecione o operador
- Informe a senha
- Escolha data, turno e valor de abertura
- Clique em "Abrir Caixa e Entrar"

### 2. Registrar Vendas
- Vá em "Vendas"
- Preencha os dados da venda
- Adicione as formas de pagamento
- Clique em "Registrar Venda"

### 3. Registrar Delivery
- Vá em "Delivery"
- Preencha os dados do pedido
- Selecione o motoboy
- Adicione as formas de pagamento
- Clique em "Registrar Delivery"

### 4. Registrar Despesas
- Vá em "Despesas"
- Selecione o tipo de despesa
- Preencha os dados
- Clique em "Registrar Despesa"

### 5. Fazer Sangria
- Vá em "Sangria"
- Informe o valor e motivo
- Clique em "Registrar Sangria"

### 6. Controlar Estoque
- Vá em "Estoque"
- Cadastre produtos
- Registre movimentações
- Acompanhe alertas de estoque baixo

### 7. Visualizar Dashboard
- Vá em "Dashboard"
- Selecione o período desejado
- Visualize gráficos e relatórios

### 8. Configurar Sistema
- Vá em "Configurações" (requer permissão de admin)
- Cadastre usuários, formas de pagamento, etc.

### 9. Fechar Caixa
- Clique em "Fechar Caixa"
- Confira todos os valores
- Confirme o fechamento
- Sistema retornará para tela de login

## 🎨 Características Técnicas

- **Backend:** Python Flask 3.0
- **Banco de Dados:** SQLAlchemy (ORM) + SQLite
- **Frontend:** Bootstrap 5.3 + Font Awesome 6
- **Gráficos:** Chart.js
- **Autenticação:** Flask Sessions + Werkzeug Security
- **Responsivo:** Design adaptável para mobile

## 🔐 Segurança

- Senhas criptografadas com hash (Werkzeug)
- Proteção de rotas com decorators
- Validação de formulários
- Controle de sessão
- Proteção contra SQL injection (SQLAlchemy ORM)

## 📝 Personalizações

### Adicionar nova forma de pagamento
1. Vá em Configurações
2. Seção "Formas de Pagamento"
3. Digite o nome e clique em "Adicionar"

### Adicionar categoria de despesa
1. Vá em Configurações
2. Seção "Categorias de Despesa"
3. Digite nome, selecione tipo e clique em "Adicionar"

### Criar novo usuário
1. Vá em Configurações
2. Seção "Usuários / Operadores"
3. Preencha os dados e selecione permissões
4. Clique em "Adicionar Usuário"

## 🐛 Solução de Problemas

### Erro ao iniciar
```bash
# Certifique-se de estar no ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstale as dependências
pip install -r requirements.txt
```

### Erro de banco de dados
```bash
# Delete o banco e deixe o sistema recriar
rm database/caixa.db
python app.py
```

### Esqueceu a senha do admin
```bash
# Execute o Python interativo
python

# Digite os comandos:
from app import app, db, Usuario
from werkzeug.security import generate_password_hash
with app.app_context():
    admin = Usuario.query.filter_by(nome='admin').first()
    admin.senha = generate_password_hash('123')
    db.session.commit()
```

## 📊 Próximas Funcionalidades (Sugestões)

- [ ] Exportação de relatórios em PDF
- [ ] Integração com impressoras fiscais
- [ ] App mobile
- [ ] API REST
- [ ] Multi-empresa
- [ ] Backup automático na nuvem
- [ ] Integração com WhatsApp
- [ ] Sistema de comandas
- [ ] Controle de mesas em tempo real

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

## 👨‍💻 Desenvolvido com

- Flask
- SQLAlchemy
- Bootstrap
- Chart.js
- Font Awesome

## 📞 Suporte

Para dúvidas ou sugestões, consulte a documentação do Flask em: https://flask.palletsprojects.com/

---

**Sistema de Caixa - Versão 1.0**  
*Desenvolvido para facilitar a gestão do seu negócio!* 💼

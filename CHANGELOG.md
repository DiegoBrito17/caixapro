# 📋 CHANGELOG - Sistema de Caixa

## Versão 1.1 (02/02/2026) - CORREÇÕES IMPORTANTES

### 🔧 Correções de Bugs

✅ **CORRIGIDO: Dados não salvavam no banco**
- Atualizado todas as queries para SQLAlchemy 2.0
- Substituído `Model.query.get()` por `db.session.get(Model, id)`
- Eliminados todos os warnings de API legada

✅ **CORRIGIDO: Cadastro de usuários não funcionava**
- Corrigido tratamento de checkboxes no formulário
- Adicionado validação de usuário duplicado
- Melhorado feedback de sucesso/erro

✅ **CORRIGIDO: Pasta database não era criada**
- Sistema agora cria automaticamente a pasta `database`
- Não requer criação manual antes de executar

### ✨ Melhorias

✅ **Validações aprimoradas em Configurações:**
- Verificação de duplicatas em todas as entidades
- Validação de campos vazios
- Mensagens de erro mais descritivas
- Feedback específico para cada ação

✅ **Scripts de instalação (Windows):**
- `instalar.bat` - Instalação automática
- `iniciar.bat` - Inicialização simplificada

✅ **Documentação expandida:**
- SOLUCAO_PROBLEMAS.md com guia completo
- README.md atualizado
- CHANGELOG.md com histórico de versões

### 🐛 Bugs Conhecidos Corrigidos

- ❌ "unable to open database file" → ✅ RESOLVIDO
- ❌ "LegacyAPIWarning" do SQLAlchemy → ✅ RESOLVIDO
- ❌ Usuários não salvavam → ✅ RESOLVIDO
- ❌ Checkboxes não funcionavam → ✅ RESOLVIDO

---

## Versão 1.0 (02/02/2026) - Lançamento Inicial

### ✨ Funcionalidades

✅ Sistema de Login e Autenticação
✅ Gestão de Vendas (Mesa/Balcão)
✅ Gestão de Delivery
✅ Controle de Despesas (Fixas, Variáveis, Saídas)
✅ Sangria/Retiradas
✅ Controle de Estoque
✅ Dashboard com gráficos
✅ Configurações completas
✅ Fechamento de caixa

### 📦 Recursos Técnicos

- Flask 3.0
- SQLAlchemy 2.0
- Bootstrap 5.3
- Chart.js
- SQLite Database
- Autenticação com senha hash

---

## 🚀 Próximas Versões (Planejado)

### Versão 1.2 (Em desenvolvimento)
- [ ] Exportação de relatórios em PDF
- [ ] Importação/Exportação de dados
- [ ] Backup automático agendado
- [ ] Temas claro/escuro

### Versão 2.0 (Futuro)
- [ ] API REST
- [ ] App Mobile
- [ ] Multi-empresa
- [ ] Integração com impressoras fiscais
- [ ] Sistema de comandas
- [ ] Controle de mesas em tempo real

---

## 📞 Reportar Bugs

Se encontrar algum bug, por favor:
1. Verifique se não está listado em "Bugs Conhecidos"
2. Consulte SOLUCAO_PROBLEMAS.md
3. Anote a mensagem de erro completa
4. Descreva os passos para reproduzir

---

**Sistema de Caixa - Versão 1.1**  
*Atualizado em 02/02/2026*

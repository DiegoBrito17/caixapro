# 🚀 INSTALAÇÃO RÁPIDA - Sistema de Caixa v2.0

## ⚡ Instalação em 3 Passos (Windows)

### 1️⃣ Extraia o ZIP
```
Descompacte sistema_caixa_v2.0_CORRIGIDO.zip
```

### 2️⃣ Execute o Instalador
```bash
# Abra o prompt de comando na pasta
# Execute:
instalar.bat
```

### 3️⃣ Inicie o Sistema
```bash
iniciar.bat
```

**Pronto!** Acesse: http://localhost:5000

---

## 🐧 Instalação Manual (Todos os Sistemas)

```bash
# 1. Navegue até a pasta
cd sistema_caixa

# 2. Crie ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instale dependências
pip install Flask Flask-SQLAlchemy Werkzeug

# 5. Execute
python app.py
```

---

## 🔑 Login Padrão

- **URL:** http://localhost:5000
- **Usuário:** admin
- **Senha:** 123

---

## ✨ Novidades v2.0

### Dashboard Avançado:
- ✅ 10+ gráficos profissionais
- ✅ Análise por turno (Manhã/Tarde/Noite)
- ✅ Ranking de motoboys
- ✅ Margem de lucro calculada
- ✅ Melhor e pior dia automático

### Gestão Admin:
- ✅ Gerenciar todos os caixas
- ✅ Editar lançamentos
- ✅ Deletar vendas/despesas
- ✅ Visualizar detalhes completos

### Métricas Financeiras:
- ✅ Lucro líquido
- ✅ Margem de lucro (%)
- ✅ Ticket médio (geral, mesa, delivery)
- ✅ Contas assinadas rastreadas
- ✅ % de notas fiscais

---

## 🔧 Solução de Problemas

### Erro: "unable to open database file"
```bash
mkdir database
```

### Erro: "No module named 'flask'"
```bash
pip install Flask Flask-SQLAlchemy Werkzeug
```

### Banco já existe da v1.1?
✅ **Compatível!** Só substituir os arquivos e executar.

---

## 📊 O que mudou da v1.1 para v2.0?

| Item | v1.1 | v2.0 |
|------|------|------|
| Gráficos | 4 | 10+ |
| Métricas | 5 | 15+ |
| Gestão Admin | ❌ | ✅ |
| Análise Turno | ❌ | ✅ |
| Conta Assinada | ❌ | ✅ |

---

## 💡 Dicas de Uso

1. **Analise os turnos** para escalar melhor sua equipe
2. **Acompanhe motoboys** para bonificar os mais produtivos
3. **Use Gestão Admin** para corrigir erros rapidamente
4. **Monitore margem** para manter lucratividade
5. **Compare dias** para identificar padrões

---

## 📞 Suporte

Consulte os arquivos:
- `README.md` - Documentação completa
- `SOLUCAO_PROBLEMAS.md` - Troubleshooting
- `ATUALIZACAO_V2.0.md` - Detalhes da versão

---

**Sistema de Caixa v2.0** 🚀  
*Gestão profissional para o seu negócio!*

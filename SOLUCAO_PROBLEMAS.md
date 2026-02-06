# 🔧 GUIA DE SOLUÇÃO DE PROBLEMAS

## ❌ Erro: "unable to open database file"

**Causa:** A pasta `database` não existe.

**Solução:**
```bash
# Crie a pasta manualmente
mkdir database

# Ou execute o instalador novamente
instalar.bat
```

---

## ❌ Erro: "No module named 'flask_sqlalchemy'"

**Causa:** Dependências não instaladas.

**Solução:**
```bash
# Ative o ambiente virtual
venv\Scripts\activate

# Instale as dependências
pip install Flask Flask-SQLAlchemy Werkzeug
```

---

## ❌ Erro: "python não é reconhecido"

**Causa:** Python não está instalado ou não está no PATH.

**Solução:**
1. Baixe e instale o Python em: https://www.python.org/downloads/
2. Durante a instalação, marque "Add Python to PATH"
3. Reinicie o terminal/prompt de comando

---

## 🚀 INSTALAÇÃO RÁPIDA (Windows)

### Opção 1: Automática (Recomendado)
```bash
# 1. Execute o instalador
instalar.bat

# 2. Execute o sistema
iniciar.bat
```

### Opção 2: Manual
```bash
# 1. Crie ambiente virtual
python -m venv venv

# 2. Ative o ambiente
venv\Scripts\activate

# 3. Instale dependências
pip install Flask Flask-SQLAlchemy Werkzeug

# 4. Crie pasta database
mkdir database

# 5. Execute o sistema
python app.py
```

---

## 🐧 INSTALAÇÃO (Linux/Mac)

```bash
# 1. Crie ambiente virtual
python3 -m venv venv

# 2. Ative o ambiente
source venv/bin/activate

# 3. Instale dependências
pip install Flask Flask-SQLAlchemy Werkzeug

# 4. Crie pasta database
mkdir -p database

# 5. Execute o sistema
python app.py
```

---

## 🔑 Acesso Padrão

- **URL:** http://localhost:5000
- **Usuário:** admin
- **Senha:** 123

---

## ❓ Perguntas Frequentes

### Como resetar a senha do admin?

Execute no terminal Python:
```python
from app import app, db, Usuario
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = Usuario.query.filter_by(nome='admin').first()
    admin.senha = generate_password_hash('123')
    db.session.commit()
    print("Senha resetada!")
```

### Como limpar o banco de dados?

1. Feche o sistema
2. Delete o arquivo `database/caixa.db`
3. Inicie o sistema novamente

### O sistema não abre no navegador?

1. Verifique se está rodando: veja se aparece "Running on http://127.0.0.1:5000"
2. Tente acessar: http://127.0.0.1:5000
3. Verifique o firewall do Windows
4. Certifique-se de que a porta 5000 não está em uso

### Erro de porta já em uso?

Altere a porta no arquivo `app.py` (última linha):
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001 ou outra porta
```

---

## 📞 Suporte Adicional

Para mais informações, consulte:
- README.md - Documentação completa
- Documentação Flask: https://flask.palletsprojects.com/
- Documentação SQLAlchemy: https://www.sqlalchemy.org/

---

**Sistema de Caixa v1.0**  
*Desenvolvido com Flask + SQLAlchemy*

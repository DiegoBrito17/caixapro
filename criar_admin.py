if __name__ == '__main__':
    from app import app, db, Usuario
    from werkzeug.security import generate_password_hash
    
    with app.app_context():
        # 🔐 dados do admin
        NOME = "admin"
        SENHA = "admin123"
        
        usuario = Usuario.query.filter_by(nome=NOME).first()
        
        if usuario:
            print("⚠️ Admin já existe")
        else:
            admin = Usuario(
                nome=NOME,
                senha=generate_password_hash(SENHA),
                perfil="ADMIN",
                ativo=True,
                acesso_configuracoes=True
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuário ADMIN criado com sucesso")

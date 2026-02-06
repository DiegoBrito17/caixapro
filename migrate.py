from app import db, app
from app import Usuario
from sqlalchemy import text

with app.app_context():
    # Adicionar coluna se não existir
    try:
        # Tentar executar SQL para adicionar coluna
        with db.engine.connect() as conn:
            conn.execute(text('ALTER TABLE usuario ADD COLUMN acesso_relatorios BOOLEAN DEFAULT 0'))
            conn.commit()
        print("✅ Coluna 'acesso_relatorios' adicionada ao banco de dados!")
    except Exception as e:
        print(f"⚠️ Coluna já existe ou erro: {e}")
    
    # Atualizar ADMINS para ter acesso a relatórios
    admins = Usuario.query.filter_by(perfil='ADMIN').all()
    for admin in admins:
        admin.acesso_relatorios = True
    db.session.commit()
    
    print("✅ Permissões de relatório atualizadas para ADMINS!")
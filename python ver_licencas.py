import sys
import os

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Licenca
from datetime import datetime

with app.app_context():
    licencas = Licenca.query.all()
    
    print("\n" + "="*70)
    print("CHAVES DE LICENÇA DO SISTEMA DE CAIXA")
    print("="*70)
    
    if licencas:
        for i, licenca in enumerate(licencas, 1):
            print(f"\n[{i}] ID: {licenca.id}")
            print(f"   E-mail: {licenca.email}")
            print(f"   Chave:  {licenca.chave_ativacao}")
            print(f"   Status: {licenca.status}")
            print(f"   Ativa:  {'SIM' if licenca.ativo else 'NÃO'}")
            
            if licenca.data_expiracao:
                dias = (licenca.data_expiracao - datetime.utcnow()).days
                status_exp = f" (Expira em {dias} dias)" if dias > 0 else f" (Expirada há {-dias} dias)"
                print(f"   Expira: {licenca.data_expiracao.strftime('%d/%m/%Y')}{status_exp}")
            
            # Dispositivos associados
            if licenca.dispositivos:
                print(f"   Dispositivos ({len(licenca.dispositivos)}):")
                for disp in licenca.dispositivos:
                    print(f"     - {disp.nome} ({disp.endereco_ip}) - {disp.status}")
    else:
        print("\n⚠️  NENHUMA LICENÇA CADASTRADA!")
        print("\nPara criar uma licença de teste, execute:")
        print("python -c \"")
        print("from app import app, db, Licenca, datetime, timedelta")
        print("import random, string")
        print("with app.app_context():")
        print("    chave = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4))")
        print("    licenca = Licenca(")
        print("        email='admin@teste.com',")
        print("        chave_ativacao=chave,")
        print("        data_expiracao=datetime.utcnow() + timedelta(days=365),")
        print("        status='ATIVA'")
        print("    )")
        print("    db.session.add(licenca)")
        print("    db.session.commit()")
        print("    print(f'Chave criada: {chave}')")
        print("\"")
    
    print("\n" + "="*70)
    
    # Oferecer opção para criar chave
    criar = input("\nDeseja criar uma chave de teste? (s/n): ").lower()
    if criar == 's':
        import random
        import string
        
        email = input("Digite o e-mail: ") or "teste@email.com"
        chave = '-'.join(
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            for _ in range(4)
        )
        
        nova_licenca = Licenca(
            email=email,
            chave_ativacao=chave,
            data_expiracao=datetime.utcnow() + timedelta(days=365),
            status='ATIVA'
        )
        db.session.add(nova_licenca)
        db.session.commit()
        
        print(f"\n✅ CHAVE CRIADA COM SUCESSO!")
        print(f"E-mail: {email}")
        print(f"Chave:  {chave}")
        print("\nCopie esta chave para usar na ativação!")
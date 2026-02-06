from app import app, db, FormaPagamento, BandeiraCartao, CategoriaDespesa


FORMAS_PAGAMENTO = [
    'Dinheiro', 'Crédito', 'Débito', 'PIX', 'Cartão (Voucher)',
    'Conta Assinada', 'PG Online', 'Link de Pagamento',
    'Transferência', 'Depósito', 'Boleto', 'Cheque',
    'Vale Refeição', 'Vale Alimentação', 'Cortesia'
]

BandeIRAS = [
    'Visa', 'Mastercard', 'Elo', 'American Express',
    'Hipercard', 'Diners Club', 'Discover', 'Aura',
    'Cabal', 'Banescard', 'Good Card', 'Sodexo',
    'Ticket', 'VR', 'Alelo'
]

CATEGORIAS = [
    ('Aluguel', 'FIXA'),
    ('Condomínio', 'FIXA'),
    ('Água', 'FIXA'),
    ('Luz', 'FIXA'),
    ('Internet', 'FIXA'),
    ('Telefonia', 'FIXA'),
    ('Contabilidade', 'FIXA'),
    ('Sistema/Software', 'FIXA'),
    ('Produtos', 'VARIAVEL'),
    ('Embalagens', 'VARIAVEL'),
    ('Gás', 'VARIAVEL'),
    ('Manutenção', 'VARIAVEL'),
    ('Limpeza', 'VARIAVEL'),
    ('Marketing', 'VARIAVEL'),
    ('Fretado/Entrega', 'VARIAVEL'),
    ('Comissão Motoboy', 'VARIAVEL'),
    ('Taxas Cartão', 'SAIDA'),
    ('Taxas Plataforma', 'SAIDA'),
    ('Impostos', 'SAIDA'),
    ('Passagem', 'SAIDA'),
    ('Multas', 'SAIDA'),
    ('Outros', 'SAIDA')
]


def main():
    with app.app_context():
        adicionados = 0

        for nome in FORMAS_PAGAMENTO:
            if not FormaPagamento.query.filter_by(nome=nome).first():
                db.session.add(FormaPagamento(nome=nome))
                adicionados += 1

        for nome in BandeIRAS:
            if not BandeiraCartao.query.filter_by(nome=nome).first():
                db.session.add(BandeiraCartao(nome=nome))
                adicionados += 1

        for nome, tipo in CATEGORIAS:
            if not CategoriaDespesa.query.filter_by(nome=nome).first():
                db.session.add(CategoriaDespesa(nome=nome, tipo=tipo))
                adicionados += 1

        db.session.commit()
        print(f"Seed concluído. Itens adicionados: {adicionados}")


if __name__ == "__main__":
    main()

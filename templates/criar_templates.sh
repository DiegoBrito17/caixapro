#!/bin/bash

echo "📝 Criando templates..."

# SUPRIMENTOS.HTML
cat > suprimentos.html << 'SUP'
{% extends "base.html" %}
{% block title %}Suprimentos{% endblock %}

{% block content %}
<div class="container-fluid">
    <div class="card">
        <div class="card-header bg-success text-white">
            <h4><i class="fas fa-hand-holding-usd me-2"></i>Suprimentos - {{ caixa.turno }} - {{ caixa.data.strftime('%d/%m/%Y') }}</h4>
        </div>
        <div class="card-body">
            <div class="card mb-4">
                <div class="card-header bg-light">
                    <h5><i class="fas fa-plus-circle me-2"></i>Adicionar Suprimento</h5>
                </div>
                <div class="card-body">
                    <form method="POST" action="{{ url_for('novo_suprimento') }}">
                        <div class="row">
                            <div class="col-md-3">
                                <label>💵 Valor (R$)</label>
                                <input type="number" step="0.01" class="form-control" name="valor" required>
                            </div>
                            <div class="col-md-4">
                                <label>📝 Motivo</label>
                                <input type="text" class="form-control" name="motivo" placeholder="Ex: Troco banco" required>
                            </div>
                            <div class="col-md-4">
                                <label>💬 Observação</label>
                                <input type="text" class="form-control" name="observacao">
                            </div>
                            <div class="col-md-1">
                                <label>&nbsp;</label>
                                <button type="submit" class="btn btn-success w-100"><i class="fas fa-plus"></i></button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header bg-info text-white">
                    <h5><i class="fas fa-history me-2"></i>Histórico ({{ suprimentos|length }})</h5>
                </div>
                <div class="card-body">
                    {% if suprimentos %}
                    <table class="table table-hover">
                        <thead class="table-light">
                            <tr>
                                <th>Hora</th>
                                <th>Motivo</th>
                                <th>Valor</th>
                                <th>Observação</th>
                                {% if usuario_logado and usuario_logado.acesso_configuracoes %}
                                <th>Ações</th>
                                {% endif %}
                            </tr>
                        </thead>
                        <tbody>
                            {% for suprimento in suprimentos %}
                            <tr>
                                <td>{{ suprimento.data_hora.strftime('%H:%M') }}</td>
                                <td>{{ suprimento.motivo }}</td>
                                <td class="text-success"><strong>+ R$ {{ "%.2f"|format(suprimento.valor) }}</strong></td>
                                <td>{{ suprimento.observacao or '-' }}</td>
                                {% if usuario_logado and usuario_logado.acesso_configuracoes %}
                                <td>
                                    <a href="{{ url_for('admin_editar_suprimento', suprimento_id=suprimento.id) }}" class="btn btn-sm btn-warning">
                                        <i class="fas fa-edit"></i>
                                    </a>
                                    <form method="POST" action="{{ url_for('admin_deletar_suprimento', suprimento_id=suprimento.id) }}" style="display:inline;" onsubmit="return confirm('⚠️ Confirma exclusão?')">
                                        <button type="submit" class="btn btn-sm btn-danger">
                                            <i class="fas fa-trash"></i>
                                        </button>
                                    </form>
                                </td>
                                {% endif %}
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                    {% else %}
                    <p class="text-muted">Nenhum suprimento registrado.</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
SUP

echo "✅ suprimentos.html"

# ADMIN_EDITAR_SUPRIMENTO.HTML
cat > admin_editar_suprimento.html << 'EDITSUP'
{% extends "base.html" %}
{% block title %}Editar Suprimento{% endblock %}

{% block content %}
<div class="container">
    <div class="card">
        <div class="card-header bg-warning">
            <h4>Editar Suprimento #{{ suprimento.id }}</h4>
        </div>
        <div class="card-body">
            <form method="POST">
                <div class="mb-3">
                    <label>Valor (R$)</label>
                    <input type="number" step="0.01" class="form-control" name="valor" value="{{ suprimento.valor }}" required>
                </div>
                <div class="mb-3">
                    <label>Motivo</label>
                    <input type="text" class="form-control" name="motivo" value="{{ suprimento.motivo }}" required>
                </div>
                <div class="mb-3">
                    <label>Observação</label>
                    <textarea class="form-control" name="observacao">{{ suprimento.observacao }}</textarea>
                </div>
                <button type="submit" class="btn btn-warning">Salvar</button>
                <a href="{{ url_for('suprimentos') }}" class="btn btn-secondary">Cancelar</a>
            </form>
        </div>
    </div>
</div>
{% endblock %}
EDITSUP

echo "✅ admin_editar_suprimento.html"

# ADMIN_EDITAR_SANGRIA.HTML
cat > admin_editar_sangria.html << 'EDITSANG'
{% extends "base.html" %}
{% block title %}Editar Sangria{% endblock %}

{% block content %}
<div class="container">
    <div class="card">
        <div class="card-header bg-warning">
            <h4>Editar Sangria #{{ sangria.id }}</h4>
        </div>
        <div class="card-body">
            <form method="POST">
                <div class="mb-3">
                    <label>Valor (R$)</label>
                    <input type="number" step="0.01" class="form-control" name="valor" value="{{ sangria.valor }}" required>
                </div>
                <div class="mb-3">
                    <label>Motivo</label>
                    <input type="text" class="form-control" name="motivo" value="{{ sangria.motivo }}" required>
                </div>
                <div class="mb-3">
                    <label>Observação</label>
                    <textarea class="form-control" name="observacao">{{ sangria.observacao }}</textarea>
                </div>
                <button type="submit" class="btn btn-warning">Salvar</button>
                <a href="{{ url_for('sangria') }}" class="btn btn-secondary">Cancelar</a>
            </form>
        </div>
    </div>
</div>
{% endblock %}
EDITSANG

echo "✅ admin_editar_sangria.html"

echo "🎉 Templates criados!"

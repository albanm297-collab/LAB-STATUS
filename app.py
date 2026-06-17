{% extends "base.html" %}
{% block titulo %}Historial de Reportes - Lab-Status{% endblock %}
{% block subtitulo %}Historial de Reportes{% endblock %}

{% block contenido %}

<div class="acciones-barra">
    <a href="{{ url_for('reportes.nuevo') }}" class="btn-primario">
        <span class="material-icons">add</span>
        Nuevo Reporte
    </a>
    <a href="{{ url_for('reportes.exportar_pdf') }}" class="btn-secundario">
        <span class="material-icons">picture_as_pdf</span>
        Exportar PDF
    </a>

    <form method="GET" class="form-busqueda">
        <select name="estado" onchange="this.form.submit()">
            <option value="">Todos los estados</option>
            <option value="pendiente"  {% if filtro_estado == 'pendiente'  %}selected{% endif %}>Pendientes</option>
            <option value="resuelto"   {% if filtro_estado == 'resuelto'   %}selected{% endif %}>Resueltos</option>
        </select>
    </form>
</div>

<div class="card">
    <div class="card-header">
        <span class="material-icons">history</span>
        Reportes ({{ reportes|length }})
    </div>
    <div class="card-body sin-padding">
        {% if reportes %}
        <table class="tabla">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Equipo</th>
                    <th>Laboratorio</th>
                    <th>Descripción</th>
                    <th>Tipo de Falla</th>
                    <th>Reportado por</th>
                    <th>Estado</th>
                    <th>Fecha</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {% for r in reportes %}
                <tr>
                    <td>{{ r.id }}</td>
                    <td><strong>{{ r.comp_codigo }}</strong></td>
                    <td>{{ r.lab_nombre or '—' }}</td>
                    <td>{{ r.descripcion }}</td>
                    <td>{{ r.tipo_falla or '—' }}</td>
                    <td>{{ r.usuario_nombre }}</td>
                    <td>
                        <span class="badge badge-{{ r.estado_reporte }}">
                            {{ r.estado_reporte }}
                        </span>
                    </td>
                    <td>{{ r.fecha[:16] }}</td>
                    <td class="td-acciones">
                        {% if r.estado_reporte == 'pendiente' %}
                        <a href="{{ url_for('reportes.resolver', id=r.id) }}"
                           class="btn-icono btn-verde" title="Marcar como resuelto"
                           onclick="return confirm('¿Marcar como resuelto?')">
                            <span class="material-icons">check_circle</span>
                        </a>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
            <div class="vacio">
                <span class="material-icons">history</span>
                <p>No hay reportes registrados.</p>
            </div>
        {% endif %}
    </div>
</div>

{% endblock %}

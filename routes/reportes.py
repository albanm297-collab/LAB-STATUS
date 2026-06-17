{% extends "base.html" %}
{% block titulo %}Laboratorios - Lab-Status{% endblock %}
{% block subtitulo %}Laboratorios{% endblock %}

{% block contenido %}

<div class="acciones-barra">
    <a href="{{ url_for('labs.nuevo') }}" class="btn-primario">
        <span class="material-icons">add</span>
        Nuevo Laboratorio
    </a>
</div>

<div class="card">
    <div class="card-header">
        <span class="material-icons">meeting_room</span>
        Lista de Laboratorios ({{ labs|length }})
    </div>
    <div class="card-body sin-padding">
        {% if labs %}
        <table class="tabla">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Nombre</th>
                    <th>Ubicación</th>
                    <th>Capacidad</th>
                    <th>Equipos</th>
                    <th>Fecha</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {% for lab in labs %}
                <tr>
                    <td>{{ lab.id }}</td>
                    <td><strong>{{ lab.nombre }}</strong></td>
                    <td>{{ lab.ubicacion or '—' }}</td>
                    <td>{{ lab.capacidad }} puestos</td>
                    <td>
                        <span class="badge badge-azul">{{ lab.total_comps }} equipos</span>
                    </td>
                    <td>{{ lab.fecha_creacion }}</td>
                    <td class="td-acciones">
                        <a href="{{ url_for('labs.editar', id=lab.id) }}"
                           class="btn-icono btn-editar" title="Editar">
                            <span class="material-icons">edit</span>
                        </a>
                        <a href="{{ url_for('labs.eliminar', id=lab.id) }}"
                           class="btn-icono btn-eliminar"
                           onclick="return confirm('¿Eliminar este laboratorio?')"
                           title="Eliminar">
                            <span class="material-icons">delete</span>
                        </a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
            <div class="vacio">
                <span class="material-icons">meeting_room</span>
                <p>No hay laboratorios registrados aún.</p>
                <a href="{{ url_for('labs.nuevo') }}" class="btn-primario">Registrar primero</a>
            </div>
        {% endif %}
    </div>
</div>

{% endblock %}

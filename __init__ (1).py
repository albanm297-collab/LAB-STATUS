{% extends "base.html" %}
{% block titulo %}Computadoras - Lab-Status{% endblock %}
{% block subtitulo %}Computadoras{% endblock %}

{% block contenido %}

<!-- Barra de acciones y búsqueda -->
<div class="acciones-barra">
    <a href="{{ url_for('comps.nueva') }}" class="btn-primario">
        <span class="material-icons">add</span>
        Nueva Computadora
    </a>

    <!-- Formulario de búsqueda -->
    <form method="GET" class="form-busqueda">
        <div class="input-icono">
            <span class="material-icons">search</span>
            <input type="text" name="q" value="{{ busqueda }}"
                   placeholder="Buscar por código, marca o modelo...">
        </div>

        <select name="estado">
            <option value="">Todos los estados</option>
            <option value="operativo" {% if filtro_estado == 'operativo' %}selected{% endif %}>Operativo</option>
            <option value="mantenimiento" {% if filtro_estado == 'mantenimiento' %}selected{% endif %}>En Mantenimiento</option>
            <option value="fuera_servicio" {% if filtro_estado == 'fuera_servicio' %}selected{% endif %}>Fuera de Servicio</option>
        </select>

        <select name="lab_id">
            <option value="">Todos los laboratorios</option>
            {% for lab in labs %}
            <option value="{{ lab.id }}" {% if filtro_lab == lab.id|string %}selected{% endif %}>
                {{ lab.nombre }}
            </option>
            {% endfor %}
        </select>

        <button type="submit" class="btn-secundario">
            <span class="material-icons">filter_list</span>
            Filtrar
        </button>
        <a href="{{ url_for('comps.lista') }}" class="btn-texto">Limpiar</a>
    </form>
</div>

<div class="card">
    <div class="card-header">
        <span class="material-icons">computer</span>
        Equipos registrados ({{ computadoras|length }})
    </div>
    <div class="card-body sin-padding">
        {% if computadoras %}
        <table class="tabla">
            <thead>
                <tr>
                    <th>Código</th>
                    <th>Marca / Modelo</th>
                    <th>Especificaciones</th>
                    <th>Laboratorio</th>
                    <th>Estado</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {% for c in computadoras %}
                <tr>
                    <td><strong>{{ c.codigo }}</strong></td>
                    <td>{{ c.marca or '—' }} {{ c.modelo or '' }}</td>
                    <td class="td-specs">
                        {% if c.procesador %}<span>CPU: {{ c.procesador }}</span>{% endif %}
                        {% if c.ram %}<span>RAM: {{ c.ram }}</span>{% endif %}
                        {% if c.disco %}<span>Disco: {{ c.disco }}</span>{% endif %}
                    </td>
                    <td>{{ c.lab_nombre or '—' }}</td>
                    <td>
                        <!-- Selector de estado con cambio rápido -->
                        <select class="select-estado select-{{ c.estado }}"
                                onchange="cambiarEstado({{ c.id }}, this.value, this)">
                            <option value="operativo" {% if c.estado == 'operativo' %}selected{% endif %}>✅ Operativo</option>
                            <option value="mantenimiento" {% if c.estado == 'mantenimiento' %}selected{% endif %}>🔧 Mantenimiento</option>
                            <option value="fuera_servicio" {% if c.estado == 'fuera_servicio' %}selected{% endif %}>❌ Fuera de servicio</option>
                        </select>
                    </td>
                    <td class="td-acciones">
                        <a href="{{ url_for('comps.editar', id=c.id) }}"
                           class="btn-icono btn-editar" title="Editar">
                            <span class="material-icons">edit</span>
                        </a>
                        <a href="{{ url_for('comps.eliminar', id=c.id) }}"
                           class="btn-icono btn-eliminar"
                           onclick="return confirm('¿Eliminar esta computadora?')"
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
                <span class="material-icons">computer</span>
                <p>No se encontraron computadoras.</p>
                {% if not busqueda %}
                    <a href="{{ url_for('comps.nueva') }}" class="btn-primario">Registrar primera</a>
                {% endif %}
            </div>
        {% endif %}
    </div>
</div>

{% endblock %}

{% block scripts %}
<script>
/**
 * Cambia el estado de una computadora sin recargar la página (AJAX)
 */
function cambiarEstado(id, nuevoEstado, selectEl) {
    const formData = new FormData();
    formData.append('estado', nuevoEstado);

    fetch(`/computadoras/estado/${id}`, {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.ok) {
            // Actualizar la clase CSS del select para cambiar el color
            selectEl.className = `select-estado select-${nuevoEstado}`;
            mostrarNotificacion('Estado actualizado', 'success');
        } else {
            mostrarNotificacion('Error al actualizar', 'error');
        }
    })
    .catch(() => mostrarNotificacion('Error de conexión', 'error'));
}
</script>
{% endblock %}

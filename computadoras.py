{% extends "base.html" %}
{% block titulo %}{{ 'Editar' if comp else 'Nueva' }} Computadora - Lab-Status{% endblock %}
{% block subtitulo %}{{ 'Editar' if comp else 'Nueva' }} Computadora{% endblock %}

{% block contenido %}

<div class="card card-form">
    <div class="card-header">
        <span class="material-icons">computer</span>
        {{ 'Editar computadora' if comp else 'Registrar nueva computadora' }}
    </div>
    <div class="card-body">
        <form method="POST">
            <div class="form-grid">

                <div class="campo-form">
                    <label for="codigo">Código del equipo *</label>
                    <input type="text" id="codigo" name="codigo"
                           value="{{ comp.codigo if comp else '' }}"
                           placeholder="Ej: LAB-A-01" required>
                </div>

                <div class="campo-form">
                    <label for="lab_id">Laboratorio</label>
                    <select id="lab_id" name="lab_id">
                        <option value="">-- Sin asignar --</option>
                        {% for lab in labs %}
                        <option value="{{ lab.id }}"
                            {% if comp and comp.lab_id == lab.id %}selected{% endif %}>
                            {{ lab.nombre }}
                        </option>
                        {% endfor %}
                    </select>
                </div>

                <div class="campo-form">
                    <label for="marca">Marca</label>
                    <input type="text" id="marca" name="marca"
                           value="{{ comp.marca if comp else '' }}"
                           placeholder="Ej: HP, Dell, Lenovo">
                </div>

                <div class="campo-form">
                    <label for="modelo">Modelo</label>
                    <input type="text" id="modelo" name="modelo"
                           value="{{ comp.modelo if comp else '' }}"
                           placeholder="Ej: ProDesk 400 G7">
                </div>

                <div class="campo-form">
                    <label for="procesador">Procesador</label>
                    <input type="text" id="procesador" name="procesador"
                           value="{{ comp.procesador if comp else '' }}"
                           placeholder="Ej: Intel Core i5-10400">
                </div>

                <div class="campo-form">
                    <label for="ram">Memoria RAM</label>
                    <input type="text" id="ram" name="ram"
                           value="{{ comp.ram if comp else '' }}"
                           placeholder="Ej: 8 GB DDR4">
                </div>

                <div class="campo-form">
                    <label for="disco">Disco Duro</label>
                    <input type="text" id="disco" name="disco"
                           value="{{ comp.disco if comp else '' }}"
                           placeholder="Ej: 500 GB SSD">
                </div>

                <div class="campo-form">
                    <label for="estado">Estado</label>
                    <select id="estado" name="estado">
                        <option value="operativo" {% if not comp or comp.estado == 'operativo' %}selected{% endif %}>
                            ✅ Operativo
                        </option>
                        <option value="mantenimiento" {% if comp and comp.estado == 'mantenimiento' %}selected{% endif %}>
                            🔧 En Mantenimiento
                        </option>
                        <option value="fuera_servicio" {% if comp and comp.estado == 'fuera_servicio' %}selected{% endif %}>
                            ❌ Fuera de Servicio
                        </option>
                    </select>
                </div>

            </div>

            <div class="form-botones">
                <button type="submit" class="btn-primario">
                    <span class="material-icons">save</span>
                    {{ 'Actualizar' if comp else 'Guardar' }}
                </button>
                <a href="{{ url_for('comps.lista') }}" class="btn-secundario">
                    <span class="material-icons">arrow_back</span>
                    Cancelar
                </a>
            </div>
        </form>
    </div>
</div>

{% endblock %}

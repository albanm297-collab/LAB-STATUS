{% extends "base.html" %}
{% block titulo %}{{ 'Editar' if lab else 'Nuevo' }} Laboratorio - Lab-Status{% endblock %}
{% block subtitulo %}{{ 'Editar' if lab else 'Nuevo' }} Laboratorio{% endblock %}

{% block contenido %}

<div class="card card-form">
    <div class="card-header">
        <span class="material-icons">meeting_room</span>
        {{ 'Editar laboratorio' if lab else 'Registrar nuevo laboratorio' }}
    </div>
    <div class="card-body">
        <form method="POST">
            <div class="form-grid">
                <div class="campo-form">
                    <label for="nombre">Nombre del laboratorio *</label>
                    <input type="text" id="nombre" name="nombre"
                           value="{{ lab.nombre if lab else '' }}"
                           placeholder="Ej: Lab de Informática A"
                           required>
                </div>

                <div class="campo-form">
                    <label for="ubicacion">Ubicación</label>
                    <input type="text" id="ubicacion" name="ubicacion"
                           value="{{ lab.ubicacion if lab else '' }}"
                           placeholder="Ej: Bloque B, Piso 2">
                </div>

                <div class="campo-form">
                    <label for="capacidad">Capacidad (número de puestos)</label>
                    <input type="number" id="capacidad" name="capacidad"
                           value="{{ lab.capacidad if lab else 0 }}"
                           min="0" max="100">
                </div>
            </div>

            <div class="form-botones">
                <button type="submit" class="btn-primario">
                    <span class="material-icons">save</span>
                    {{ 'Actualizar' if lab else 'Guardar' }}
                </button>
                <a href="{{ url_for('labs.lista') }}" class="btn-secundario">
                    <span class="material-icons">arrow_back</span>
                    Cancelar
                </a>
            </div>
        </form>
    </div>
</div>

{% endblock %}

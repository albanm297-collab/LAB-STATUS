<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block titulo %}Lab-Status{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <!-- Iconos de Material Design (Google) -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

<!-- ===== SIDEBAR (menú lateral) ===== -->
<aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
        <span class="material-icons logo-icon">monitor</span>
        <span class="logo-texto">Lab-Status</span>
    </div>

    <nav class="sidebar-nav">
        <a href="{{ url_for('dashboard.index') }}" class="nav-item {% if request.endpoint == 'dashboard.index' %}active{% endif %}">
            <span class="material-icons">dashboard</span>
            <span>Panel Principal</span>
        </a>
        <a href="{{ url_for('labs.lista') }}" class="nav-item {% if 'labs' in request.endpoint %}active{% endif %}">
            <span class="material-icons">meeting_room</span>
            <span>Laboratorios</span>
        </a>
        <a href="{{ url_for('comps.lista') }}" class="nav-item {% if 'comps' in request.endpoint %}active{% endif %}">
            <span class="material-icons">computer</span>
            <span>Computadoras</span>
        </a>
        <a href="{{ url_for('reportes.nuevo') }}" class="nav-item {% if request.endpoint == 'reportes.nuevo' %}active{% endif %}">
            <span class="material-icons">report_problem</span>
            <span>Reportar Falla</span>
        </a>
        <a href="{{ url_for('reportes.lista') }}" class="nav-item {% if request.endpoint == 'reportes.lista' %}active{% endif %}">
            <span class="material-icons">history</span>
            <span>Historial</span>
        </a>
    </nav>

    <div class="sidebar-footer">
        <div class="usuario-info">
            <span class="material-icons">account_circle</span>
            <span>{{ session.get('usuario_nombre', 'Usuario') }}</span>
        </div>
        <a href="{{ url_for('auth.logout') }}" class="btn-logout">
            <span class="material-icons">logout</span>
        </a>
    </div>
</aside>

<!-- ===== CONTENIDO PRINCIPAL ===== -->
<main class="contenido">
    <!-- Barra superior -->
    <header class="topbar">
        <button class="btn-menu" onclick="toggleSidebar()">
            <span class="material-icons">menu</span>
        </button>
        <h1 class="topbar-titulo">{% block subtitulo %}{% endblock %}</h1>
    </header>

    <!-- Mensajes flash (notificaciones) -->
    {% with mensajes = get_flashed_messages(with_categories=true) %}
        {% if mensajes %}
            {% for categoria, mensaje in mensajes %}
                <div class="alerta alerta-{{ categoria }}">
                    <span class="material-icons">
                        {% if categoria == 'success' %}check_circle{% else %}error{% endif %}
                    </span>
                    {{ mensaje }}
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <!-- Aquí va el contenido de cada página -->
    <div class="pagina-contenido">
        {% block contenido %}{% endblock %}
    </div>
</main>

<script src="{{ url_for('static', filename='js/main.js') }}"></script>
{% block scripts %}{% endblock %}
</body>
</html>

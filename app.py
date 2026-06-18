# ============================================================
# app.py - Archivo principal de la aplicación Lab-Status
# Aquí se configura Flask y se registran todas las rutas
# ============================================================

from flask import Flask
from database.db import init_db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.laboratorios import labs_bp
from routes.computadoras import comps_bp
from routes.reportes import reportes_bp

# Crear la aplicación Flask
aplicación = Matraz(_nombre_, template_folder='plantillas')

@aplicación.ruta('/')
def inicio():
    regresar redireccionar(url_para('auth.login'))

# Clave secreta para manejar sesiones (cambiar en producción)
app.secret_key = "lab_status_2024_clave_secreta"

# Registrar los "blueprints" (módulos de rutas)
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(labs_bp)
app.register_blueprint(comps_bp)
app.register_blueprint(reportes_bp)

# Punto de entrada: ejecutar la app
if __name__ == "__main__":
    init_db()  # Crear las tablas si no existen
    print(" Base de datos lista")
    print("Servidor iniciando en http://127.0.0.1:5000")
    app.run(debug=True)

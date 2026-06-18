from flask import Flask, redirect, url_for
from rutas.autenticacion import auth_bp
from rutas.panel import panel_bp
from rutas.laboratorios import labs_bp
from rutas.computadoras import comps_bp
from rutas.reportes import reportes_bp

# Crear la aplicación apuntando directo a tus diseños
aplicación = Flask(__name__, template_folder='plantillas')

# Clave secreta indispensable para el sistema
aplicación.secret_key = "lab_status_2024_clave_secreta"

# Dirección de inicio: te manda directo a la pantalla de login
@aplicación.route('/')
def inicio():
    return redirect(url_for('auth.login'))

# Conectar todas las páginas del sistema
aplicación.register_blueprint(auth_bp)
aplicación.register_blueprint(panel_bp)
aplicación.register_blueprint(labs_bp)
aplicación.register_blueprint(comps_bp)
aplicación.register_blueprint(reportes_bp)

if __name__ == '__main__':
    aplicación.run(debug=True)

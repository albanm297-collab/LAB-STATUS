from flask import Flask, redirect, url_for
from base_datos.base_de_datos import init_db
from rutas.autenticacion import auth_bp
from rutas.panel import panel_bp
from rutas.laboratorios import labs_bp
from rutas.computadoras import comps_bp
from rutas.reportes import reportes_bp

# Crear la aplicación Flask con la carpeta en español
aplicación = Flask(__name__, template_folder='plantillas')

# Clave secreta para manejar sesiones
aplicación.secret_key = "lab_status_2024_clave_secreta"

# Ruta para la página de inicio que te manda directo al login
@aplicación.route('/')
def inicio():
    return redirect(url_for('auth.login'))

# Registrar las rutas oficiales de tu sistema
aplicación.register_blueprint(auth_bp)
aplicación.register_blueprint(panel_bp)
aplicación.register_blueprint(labs_bp)
aplicación.register_blueprint(comps_bp)
aplicación.register_blueprint(reportes_bp)

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    aplicación.run(debug=True)

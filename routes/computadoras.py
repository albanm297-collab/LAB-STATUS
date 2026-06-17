from flask import Blueprint, render_template

computadoras_bp = Blueprint('computadoras', __name__)

@computadoras_bp.route('/computadoras')
def computadoras():
    return render_template('computadoras.html')

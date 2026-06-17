from flask import Blueprint, render_template

comps_bp = Blueprint('computadoras', __name__)

@comps_bp.route('/computadoras')
def computadoras():
    return render_template('computadoras.html')

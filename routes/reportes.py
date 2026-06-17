from flask import Blueprint, render_template

informes_bp = Blueprint('informes', __name__)

@informes_bp.route('/informes')
def informes():
    return render_template('informes.html')

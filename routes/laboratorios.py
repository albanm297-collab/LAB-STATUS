from flask import Blueprint, render_template

labs_bp = Blueprint('laboratorios', _name_)

@labs_bp.route('/laboratorios')
def laboratorios():
    return render_template('laboratorios.html')

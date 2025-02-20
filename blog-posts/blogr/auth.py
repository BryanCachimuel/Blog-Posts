from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register')
def register():
    return 'Página de Registro'

@bp.route('/login')
def login():
    return 'Página de Inicio de Sesión'

@bp.route('/profile')
def profile():
    return 'Página de Perfil'
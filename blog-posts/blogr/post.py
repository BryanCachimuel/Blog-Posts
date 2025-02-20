from flask import Blueprint

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/posts')
def posts():
    return 'Página de Publicaciones'

@bp.route('/create')
def create():
    return 'Página de Creación de Publicaciones'

@bp.route('/update')
def update():
    return 'Página de Actualización de Publicaciones'
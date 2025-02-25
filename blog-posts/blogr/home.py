from flask import Blueprint, render_template, request

from .models import User, Post

bp = Blueprint('home', __name__)

# Se obtiene un usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

# función para dar funcionalidad al buscador
def search_posts(query):
    # ilike -> recibe los textos que se le van a enviar por el buscador y va a encontrar todas las coincidencias y por ende nos devuelve el dato buscado
    posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
    return posts


@bp.route('/', methods=['GET','POST'])
def index():
    # recuperando todos los blogs
    posts = Post.query.all()

    # proceso para el funcionamiento del buscador de posts
    if request.method == 'POST':
        query = request.form.get('search')
        posts = search_posts(query)
        value = 'hidden'
        return render_template('index.html', posts = posts, get_user = get_user, value =  value)

    return render_template('index.html', posts = posts, get_user = get_user)

@bp.route('/blog/<url>')
def blog(url):
    # buscar un registro en la base de datos mediante url
    post = Post.query.filter_by(url = url).first()
    return render_template('blog.html', post = post, get_user = get_user)
from flask import Flask

# Importando el proceso para la conexión hacia la base de datos
from flask_sqlalchemy import SQLAlchemy

# Instancia para la base de datos
db = SQLAlchemy()

# Importando los modelos
from .models import User, Post

# importando las vistas creadas desde home.py
from blogr import home

# importando las vistas creadas desde auth.py
from blogr import auth

# importando las vistas creadas desde post.py
from blogr import post

def create_app():

    # Crear la aplicación de flask
    app = Flask(__name__)

    # Importando la configuración de la clase Config realizada en el archivo config.py
    app.config.from_object('config.Config')

    # Inicializando la base de datos
    db.init_app(app)

    # registrar el Blueprint de home
    app.register_blueprint(home.bp)

    # registrar el Blueprint de auth    
    app.register_blueprint(auth.bp)

    # registrar el Blueprint de post 
    app.register_blueprint(post.bp)

    # migrar todos los modelos creados
    with app.app_context():
        db.create_all()

    return app
from flask import Flask

# importando las vistas creadas desde home.py
from blogr import home

# importando las vistas creadas desde auth.py
from blogr import auth

# importando las vistas creadas desde post.py
from blogr import post

def create_app():

    # Crear la aplicación de flask
    app = Flask(__name__)

    # registrar el Blueprint de home
    app.register_blueprint(home.bp)

    # registrar el Blueprint de auth    
    app.register_blueprint(auth.bp)

    # registrar el Blueprint de post 
    app.register_blueprint(post.bp)

    return app
from flask import Flask

def create_app():

    # Crear la aplicación de flask
    app = Flask(__name__)

    @app.route('/')
    def hola():
        return 'Hola desde el proyecto'

    return app
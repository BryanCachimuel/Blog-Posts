# conexiones preparadas para cualquier base de datos
SQLITE = "sqlite:///blogposts_db"
POSTGRESQL = "postgresql+psycopg2://postgres:admin1994@localhost:5432/blogposts_db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    # conexión realizada hacia la base de datos
    SQLALCHEMY_DATABASE_URI = POSTGRESQL

    # agregando la librería ckeditor
    CKEDITOR_PKG_TYPE = 'basic'
from blogr import db

# Creando el modelo para User
class User(db.Model):
    __tablename__ = 'users' # se indica el nombre con el que se va a crear la tabla
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))

    # constructor
    def __init__(self, username, email, password, photo = None):
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo

    def __repr__(self):
        return f"User: '{self.username}'"
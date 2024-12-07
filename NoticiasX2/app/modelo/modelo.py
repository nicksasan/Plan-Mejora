
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    superadmin = db.Column(db.Boolean, default=False)  # Nuevo campo para indicar si es superadmin


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    contrasena = db.Column(db.String(250))
    rolid = db.Column(db.Integer, db.ForeignKey('rol.id'))

    @property
    def contrasena(self):
        raise AttributeError("La contraseña es incorrecta.")

    @contrasena.setter
    def contrasena(self, password):
        self.contrasena_hash = generate_password_hash(password)

    def verificar_contrasena(self, password):
        return check_password_hash(self.contrasena_hash, password)
    
    @property
    def es_superadmin(self):
        return self.rol.superadmin
    
class Noticias(db.Model):
    __tablename__='noticias'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    contenido = db.Column(db.String(300))

class Comentarios(db.Model):
    __tablename__='comentarios'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(350))
    calificacion = db.Column(db.Integer)
    idusu=db.Column(db.Integer, db.ForeignKey('usuario.id'))
    idnoti=db.Column(db.Integer, db.ForeignKey('noticias.id'))



class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        load_instance = True
    
class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True

class NoticiasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Noticias
        load_instance = True

class ComentariosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comentarios
        load_instance = True
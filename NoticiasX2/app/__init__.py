from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from .modelo import db
from .vistas import ActualizacionRol, CreacionRol, VistaLogin, VistaComentarios, VistaNoticias, VistasSignIn, VistaUsuario
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) #Carga la configuración desde config.py
    CORS(app) #Habilita CORS
    db.init_app(app) #Inicializa SQLAlchemy
    Migrate(app, db) #Configura Flask-Migrate
    JWTManager(app) #Configura JWT


    #Configuta la API
    api = Api(app)
    api.add_resource(VistaLogin, '/Registro')
    api.add_resource(VistasSignIn, '/SignIn')
    api.add_resource(ActualizacionRol, '/ActualizarRol', '/ActualizarRol/<int:id>')
    api.add_resource(CreacionRol, '/CrearRol')
    api.add_resource(VistaNoticias, '/Noticias', '/Noticias/<int:id>')
    api.add_resource(VistaComentarios, '/Comentarios', '/Comentarios/<int:id>')
    api.add_resource(VistaUsuario, '/Usuario', '/Usuario/<int:id>')



    return app
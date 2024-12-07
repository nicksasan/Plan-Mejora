import os 

class Config:
    #Configuración de la base de datos
    USER_DB = 'root'
    PASSWORD_DB = ''
    URL_DB = 'localhost'
    NAME_DB = 'Noticias'
    FULL_URL_DB = f'mysql://{USER_DB}:{PASSWORD_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Corregido
    JWT_SECRET_KEY = 'nisnitalatam123'
    PROPAGATE_EXCEPTIONS = True

config = {
    'default': Config
}
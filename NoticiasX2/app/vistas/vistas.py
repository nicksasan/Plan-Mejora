
from flask import request
from flask_restful import Resource
from ..modelo import db, Usuario, UsuarioSchema, Noticias, NoticiasSchema, Comentarios, ComentariosSchema, Rol, RolSchema
from flask_jwt_extended import jwt_required, create_access_token

usuario_schema = UsuarioSchema()
noticias_schema = NoticiasSchema()
comentarios_schema = ComentariosSchema()
rol_schema = RolSchema()


class VistaUsuario(Resource):
    def get(self):
        return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]
    
    def post(self):
        nuevo_usuario = Usuario (
            nombre=request.json['nombre'],
            correo=request.json['correo'],
            contrasena=request.json['contrasena']
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.dump(nuevo_usuario), 201
    
    def put(self, id):
        usuario = Usuario.query.get_or_404(id)
        usuario.nombre = request.json['nombre']
        usuario.correo = request.json['correo']
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204

class VistaLogin(Resource):
    @jwt_required
    def post(self):
        u_correo = request.json['correo']
        u_contrasena = request.json['contrasena']
        usuario = Usuario.query.filter_by(correo=u_correo).first()
        if usuario and usuario.verificar_contrasena(u_contrasena):
            return {'mensaje': 'Inicio de sesión exitoso.'}, 200

        else: 
            return { 'mensaje': 'Correo o contraseña incorrecta.' }, 400
        
class VistasSignIn(Resource):
    @jwt_required
    def post(self):
        nuevo_usuario = Usuario (
            nombre=request.json['nombre'],
            correo=request.json['correo'],
            contrasena=request.json['contrasena']
        )
        token_de_acceso = create_access_token(identity=request.json['correo'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return { 'mensaje': 'Registro exitoso.', 'token_de_acceso': token_de_acceso }, 201
    


class VistaNoticias(Resource):
    def get(self):
        return [noticias_schema.dump(noticia) for noticia in Noticias.query.all()]
    
    def post(self):
        nuevo_noticia = Noticias (
            titulo=request.json['titulo'],
            contenido=request.json['contenido']
        )
        db.session.add(nuevo_noticia)
        db.session.commit()
        return noticias_schema.dump(nuevo_noticia), 201
    
    def put(self, id):
        noticia = Noticias.query.get_or_404(id)
        noticia.titulo = request.json['titulo']
        noticia.contenido = request.json['contenido']
        db.session.commit()
        return noticias_schema.dump(noticia)

    def delete(self, id):
        noticia = Noticias.query.get_or_404(id)
        db.session.delete(noticia)
        db.session.commit()
        return '', 204
    
class VistaComentarios(Resource):
    def get(self):
        return [comentarios_schema.dump(comentario) for comentario in Comentarios.query.all()]
    
    def post(self):
        nuevo_comentario = Comentarios (
            texto=request.json['texto'],
            calificacion=request.json['calificacion'],
            idusu=request.json['idusu'],
            idnot=request.json['idnot']
        )
        db.session.add(nuevo_comentario)
        db.session.commit()
        return comentarios_schema.dump(nuevo_comentario), 201
    
    def put(self, id):
        comentario = Comentarios.query.get_or_404(id)
        comentario.texto = request.json['texto']
        comentario.calificacion = request.json['calificacion']
        comentario.idusu = request.json['idusu']
        comentario.idnot = request.json['idnot']
        db.session.commit()
        return comentarios_schema.dump(comentario)
    
    def delete(self, id):
        comentario = Comentarios.query.get_or_404(id)
        db.session.delete(comentario)
        db.session.commit()
        return '', 204
    
class ActualizacionRol(Resource):
    def get(self):
        return [rol_schema.dump(rol) for rol in Rol.query.all()]
    
    def post(self):
        nuevo_rol = Rol (
            superadmin=request.json['superadmin']
        )
        db.session.add(nuevo_rol)
        db.session.commit()
        return rol_schema.dump(nuevo_rol), 201
    
    def put(self, id):
        rol = Rol.query.get_or_404(id)
        rol.superadmin = request.json['superadmin']
        db.session.commit()
        return rol_schema.dump(rol)
    
    def delete(self, id):
        rol = Rol.query.get_or_404(id)
        db.session.delete(rol)
        db.session.commit()
        return '', 204
    
class CreacionRol(Resource):
    def post(self):
        nuevo_rol = Rol (
            superadmin=request.json['superadmin']
        )
        db.session.add(nuevo_rol)
        db.session.commit()
        return rol_schema.dump(nuevo_rol), 201
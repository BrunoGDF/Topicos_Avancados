from flask import Flask
from flask_restful import Resource, Api
from getGenders import getGenders
from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

#Model
#from model.usuario import Usuario
#from model.genero import Genero

app = Flask(__name__)
api = Api(app)

test = '{"gender1": "action", "gender2": "terror", "gender3": "comedy"}'

generos = ['Ação','Adulto','Aventura','Animação','Biografia','Comédia','Crime','Documentário','Drama','Família','Fantasia','Film Noir','Game show','História','Horror','Musical','Música','Mistério','Notícia','Reality show','Romance','Ficção científica','Curta-metragem','Esporte','Programa de entrevistas','Suspense','Guerra','Ocidental']
grupos = ['Grupo 1','Grupo 2','Grupo 3']

class setDadosIniciais(Resource):
    def get(self):
        db_string = "postgres://fatec:fatec@postgres:5432/pi"
        db = create_engine(db_string)  
        base = declarative_base()

        class Genero(base):
            __tablename__ = 'Genero'
            id = Column(Integer, primary_key=True)
            tipo = Column(String)
        
        class Usuario(base):
            __tablename__ = 'Usuario'
            id = Column(Integer, primary_key=True)
            desc = Column(String)

        Session = sessionmaker(db)  
        session = Session()
        base.metadata.create_all(db)

        # Create
        for genero in generos:
            g = Genero(tipo=genero)
            session.add(g)
        for grupo in grupos:
            g = Usuario(desc=grupo)
            session.add(g)
        session.commit()
        return {
            'Msg': 'Cadastrado com sucesso.'
        }


class setGenero(Resource):
    def get(self,usuario, genero):
        db_string = "postgres://fatec:fatec@postgres:5432/pi"
        db = create_engine(db_string)  
        base = declarative_base()

        class Genero(base):
            __tablename__ = 'Genero'
            id = Column(Integer, primary_key=True)
            tipo = Column(String)
        
        class UsuarioGenero(base):
            __tablename__ = 'UsuarioGenero'
            id_usuario = Column(Integer, primary_key=True)
            id_genero = Column(Integer, primary_key=True)

        Session = sessionmaker(db)  
        session = Session()
        base.metadata.create_all(db)

        # Read
        genero_id = 0
        generos_banco = session.query(Genero)  
        for g in generos_banco:  
            if(g.tipo==genero):
                genero_id = g.id
                break

        # Create 
        usuario_genero = UsuarioGenero(id_usuario=usuario, id_genero=genero_id)  
        session.add(usuario_genero)  
        session.commit()
        return {
            'Msg': 'Genero '+genero+' cadastrado para o usuario '+usuario+'.'
        }
#    def get(self):
#        genders = getGenders(test)
#        return genders

#api.add_resource(Test, '/')
api.add_resource(setGenero, '/setGenero/<string:usuario>/<string:genero>')
api.add_resource(setDadosIniciais, '/dadosIniciais')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.student import Student
from model.Charger import Charger
# TODO: Precisa adicionar os outros modelos (Pipeline, Carregador, Avaliador ...)

db_path = "database/"
# Verifica se o diretório existe
if not os.path.exists(db_path):
    # cria o diretório
    os.makedirs(db_path)

# url de acesso ao banco
db_url = 'sqlite://%s/students.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

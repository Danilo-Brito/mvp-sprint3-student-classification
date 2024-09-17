from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

#  TODO: Trocar essa tag
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

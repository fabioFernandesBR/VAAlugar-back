from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Canoa, Localidade
from logger import logger
from schemas import *

from flask_cors import CORS

info = Info(title="VAAlugar", version="0.1.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
canoa_tag = Tag(name="Canoa", description="Busca de canoas")
#comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/canoas', tags=[canoa_tag],
         responses={"200": SchemaListagemCanoas, "404": SchemaMensagemErro})
def get_canoas():
    """Faz a busca por TODAS AS CANOAS CADASTRADAS

    Retorna uma representação da listagem de canoas.
    """
    logger.debug(f"Coletando canoas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    canoas = session.query(Canoa).all()

    if not canoas:
        # se não há canoas cadastradas
        return {"canoas": []}, 200
    else:
        logger.debug(f"%d canoas encontradas" % len(canoas))
        # retorna a representação das canoas
        print(canoas)
        return apresenta_canoas(canoas), 200


@app.get('/canoas', tags=[canoa_tag],
         responses={"200": SchemaListagemCanoas, "404": SchemaMensagemErro})
def get_canoas_por_tipo(query: SchemaBuscaCanoaPorTipo):
    """
    # Faz a busca por canoas a partir do TIPO

    # Retorna uma representação das canoas que atendem a este tipo.
    """
    canoa_tipo = query.tipo
    logger.debug(f"Coletando dados sobre canoas #{canoa_tipo}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    canoas = session.query(Canoa).filter(Canoa.tipo == canoa_tipo).all() ###AQUI

    if not canoas:
        # se o produto não foi encontrado
        error_msg = "Canoa não encontrada na base :/"
        logger.warning(f"Erro ao buscar canoa '{canoa_tipo}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Canoas encontradas: '{canoa_tipo}'")
        # retorna a representação de produto
        return apresenta_canoas(canoas), 200



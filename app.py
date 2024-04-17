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
local_tag = Tag(name = "Local", description = "Busca de locais para remar!")
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


@app.get('/tipo', tags=[canoa_tag],
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


@app.get('/por-municipio', tags=[canoa_tag],
         responses={"200": SchemaListagemCanoas, "404": SchemaMensagemErro})
def get_canoas_por_municipio(query: SchemaBuscaCanoaPorMunicipio):
    """
    # Faz a busca por canoas a partir do MUNICIPIO

    # Retorna uma representação das canoas que localizadas neste município.
    """
    local_buscado = query.municipio
    logger.debug(f"Coletando dados sobre canoas em #{local_buscado}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    locais = session.query(Localidade).filter(Localidade.municipio == local_buscado).all()
    canoas = session.query(Canoa).filter(Canoa.local in locais).all()

    if not canoas:
        # se a canoa não foi encontrada
        error_msg = "nenhuma canoa encontrada nesta cidade :/"
        logger.warning(f"Erro ao buscar canoa em '{local_buscado}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Canoas encontradas em: '{local_buscado}'")
        # retorna a representação de produto
        return apresenta_canoas(canoas), 200



@app.get('/locais', tags=[local_tag],
         responses={"200": SchemaListagemLocalidades, "404": SchemaMensagemErro})
def get_locais():
    """Faz a busca por TODOS OS LOCAIS CADASTRADOS

    Retorna uma representação da listagem de locais.
    """
    logger.debug(f"Coletando locais ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    localidades = session.query(Localidade).all()

    if not localidades:
        # se não há locais cadastrados
        return {"locais": []}, 200
    else:
        logger.debug(f"%d locais encontrados" % len(localidades))
        # retorna a representação dos locais / localidades
        print(localidades)
        return apresenta_localidades(localidades), 200
    

@app.get('/cidades', tags=[local_tag],
         responses={"200": SchemaListagemLocalidades, "404": SchemaMensagemErro})
def get_localidades_por_tipo(query: SchemaBuscaLocalidadePorMunicipio):
    """
    # Faz a busca por localidades a partir do MUNICIPIO

    # Retorna uma representação dos locais onde haja canoas disponíveis em determinado município.
    """
    cidade = query.municipio
    logger.debug(f"Coletando dados sobre canoas #{cidade}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    localidades = session.query(Localidade).filter(Localidade.municipio == cidade).all() ###AQUI

    if not localidades:
        # se o local não foi encontrado
        error_msg = "Não foram encontrados locais para remar neste município :/"
        logger.warning(f"Erro ao buscar município '{cidade}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Localidades encontradas em: '{cidade}'")
        # retorna a representação de produto
        return apresenta_localidades(localidades), 200
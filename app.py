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

"""
@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """ 
    # Adiciona um novo Produto à base de dados

    # Retorna uma representação dos produtos e comentários associados.
"""
    produto = Produto(
        nome=form.nome,
        quantidade=form.quantidade,
        valor=form.valor)
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400
"""

@app.get('/canoas', tags=[canoa_tag],
         responses={"200": SchemaListagemCanoas, "404": SchemaErro})
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

"""
@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
"""
    # Faz a busca por um Produto a partir do id do produto

    # Retorna uma representação dos produtos e comentários associados.
"""
    produto_nome = query.nome
    logger.debug(f"Coletando dados sobre produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first() ###AQUI

    if not produto:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{produto.nome}'")
        # retorna a representação de produto
        return apresenta_produto(produto), 200
"""

"""
@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
"""
    # Deleta um Produto a partir do nome de produto informado

    # Retorna uma mensagem de confirmação da remoção.
"""
    produto_nome = unquote(unquote(query.nome))
    print(produto_nome)
    logger.debug(f"Deletando dados sobre produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{produto_nome}")
        return {"mesage": "Produto removido", "id": produto_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
"""

"""
@app.post('/cometario', tags=[comentario_tag],
          responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
"""
    # Adiciona de um novo comentário à um produtos cadastrado na base identificado pelo id

    # Retorna uma representação dos produtos e comentários associados.
"""
    produto_id  = form.produto_id
    logger.debug(f"Adicionando comentários ao produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo produto
    produto = session.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        # se produto não encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao produto
    produto.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário ao produto #{produto_id}")

    # retorna a representação de produto
    return apresenta_produto(produto), 200
"""
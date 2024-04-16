from pydantic import BaseModel
from typing import Optional, List
from model.canoa import Canoa


# from schemas import ComentarioSchema

class SchemaBuscaCanoaPorTipo(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. 
        Que será feita apenas com base no TIPO de canoa.
    """
    tipo: str = "OC6" #Por padrão, sugiro buscar OC6


class SchemaCanoa(BaseModel):
    """ Define como uma nova canoa a ser inserida deve ser representada.
        Obs.: não faz parte do escopo do app inserir canoas via API. No entanto uso esta classe como entrada para outras classes.
    """
    nome: str = "Moana"
    tipo: str = "OC6"
    dono: str = "Bravus" 
    telefone: int = 21999999998 
    local: int = 1


class SchemaListagemCanoas(BaseModel):
    """ Define como uma listagem de canoas será retornada.
    """
    canoas:List[SchemaCanoa]


class SchemaVisualizacaoCanoas(BaseModel):
    """ Define como uma canoa será retornada.
    """
    id: int = 1
    nome: str = "Moana"
    tipo: str = "OC6"
    dono: str = "Bravus" 
    telefone: int = 21999999998 
    local: int = 1

def apresenta_canoa(canoa: Canoa):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": canoa.id,
        "nome": canoa.nome,
        "tipo": canoa.tipo,
        "dono": canoa.dono,
        "telefone": canoa.telefone,
        "local": canoa.local
       
    }

def apresenta_canoas(canoas: List[Canoa]):
    """ Retorna uma representação da canoa seguindo o schema definido em
        SchemaVisualizacaoCanoas.
    """
    result = []
    for canoa in canoas:
        result.append({
           "id": canoa.id,
            "nome": canoa.nome,
            "tipo": canoa.tipo,
            "dono": canoa.dono,
            "telefone": canoa.telefone,
            "local": canoa.local
        })

    return {"canoas": result}

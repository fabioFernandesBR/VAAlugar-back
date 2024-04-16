from pydantic import BaseModel
from typing import Optional, List
from model.localidade import Localidade


class SchemaLocalidade(BaseModel):
    """ Define como uma nova localidade a ser inserida deve ser representada.
        Obs.: não faz parte do escopo do app inserir localidades via API. No entanto uso esta classe como entrada para outras classes.
    """
    estado: str = "RJ"
    municipio: str = "Rio de Janeiro"
    bairro: str = "Recreio" 
    referencia: str = "Posto 12 - Pedra do Pontal" 

class SchemaBuscaLocalidadePorMunicipio(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. 
        Que será feita apenas com base no MUNICIPIO.
    """
    municipio: str = "Rio de Janeiro" #Por padrão, sugiro buscar Rio de Janeiro

class SchemaVisualizacaoLocalidade(BaseModel):
    """ Define como uma localidade será retornada.
    """
    #id: int = 1
    estado: str = "RJ"
    municipio: str = "Rio de Janeiro"
    bairro: str = "Recreio" 
    referencia: str = "Posto 12 - Pedra do Pontal"



class SchemaListagemLocalidades(BaseModel):
    """ Define como uma listagem de localidades será retornada.
    """
    locais:List[SchemaLocalidade]


    

def apresenta_localidade(localidade: Localidade):
    """ Retorna uma representação da localidade seguindo o schema definido em
        SchemaVisualizacaoLocalidade.
    """
    return {
        "estado": localidade.estado,
        "município": localidade.municipio,
        "bairro": localidade.bairro,
        "referencia": localidade.referencia
    }

def apresenta_localidades(localidades: List[Localidade]):
    """ Retorna uma representação das localidades seguindo o schema definido em
        SchemaVisualizacaoLocalidade.
    """
    result = []
    for localidade in localidades:
        result.append({
           "estado": localidade.estado,
           "município": localidade.municipio,
           "bairro": localidade.bairro,
           "referencia": localidade.referencia
        })

    return {"localidades": result}

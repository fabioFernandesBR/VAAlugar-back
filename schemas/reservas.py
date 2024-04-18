from pydantic import BaseModel
from typing import Optional, List
from model.reservas import Reserva


class SchemaCriacaoReserva(BaseModel):
    """ Define como uma nova reserva a ser criada deve ser representada, do usuário para a API.
        Obs.: no momento do uso deste Schema, estamos fazendo a reserva, com usuario, canoa e data. Comentario e avaliação serão submetidos em um momento posterior.
    """
    usuario: int = 21999999999
    canoa: int = 1
    data: str = "01/05/2024" 

class SchemaBuscaReservaPorTelefone(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. 
        Que será feita apenas com base no numero de TELEFONE do usuario.
    """
    telefone: int = 21999999999 #Por padrão, sugiro 21999999999    

class SchemaVisualizacaoReserva(BaseModel):
    """ Define como uma nova reserva recém criada deve ser representada, da API para o usuário.
        Obs.: no momento do uso deste Schema, estamos fazendo a reserva, com usuario, canoa e data. Comentario e avaliação serão submetidos em um momento posterior.
    """
    id_reserva: int = 1
    usuario: int = 21999999999
    canoa: int = 1
    data: str = "01/05/2024"
    comentario: str = "Topperson"
    avaliacao: int = 5


class SchemaListagemReservas(BaseModel): 
    """ Define como uma listagem de canoas será retornada.
    """
    reservas:List[SchemaVisualizacaoReserva]

class SchemaGetComentario(BaseModel):
    """ Atualiza uma reserva, incluindo comentario e avaliacao
    """
    id_reserva: int = 1
    comentario: str = "Topperson"
    avaliacao: int = 5

class SchemaRespostaComentario(BaseModel):
    """ Para confirmar a atualizacao da reserva com o comentario e a avaliacao
    """
    id_reserva: int = 1
    usuario: int = 21999999999
    canoa: int = 1
    data: str = "01/05/2024"
    comentario: str = "Topperson"
    avaliacao: int = 5



def apresenta_reserva(reserva: Reserva):
    """ Retorna uma representação da reserva seguindo o schema definido em
        SchemaVisualizacaoReserva.
    """
    return {
        "id-reserva": reserva.id,
        "usuario": reserva.usuario,
        "canoa": reserva.canoa,
        "data": reserva.data    
    }

def apresenta_reservas(reservas: list[Reserva]):
    """ Retorna uma representação das reserva seguindo o schema definido em
        SchemaListagemReservas.
    """
    result = []
    for reserva in reservas:
        result.append({
            "id-reserva": reserva.id,
            "usuario": reserva.usuario,
            "canoa": reserva.canoa,
            "data": reserva.data  
        })

    return {"reservas": result}
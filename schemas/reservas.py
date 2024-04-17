from pydantic import BaseModel
from typing import Optional, List
from model.reservas import Reserva


class SchemaCriacaoReserva(BaseModel):
    """ Define como uma nova reserva a ser criada deve ser representada, do usuário para a API.
        Obs.: no momento do uso deste Schema, estamos fazendo a reserva, com usuario, canoa e data. Comentario e avaliação serão submetidos em um momento posterior.
    """
    usuario: int = "21999999999"
    canoa: int = 1
    data: str = "01/05/2024" 
    

class SchemaVisualizacaoReserva(BaseModel):
    """ Define como uma nova reserva recém criada deve ser representada, da API para o usuário.
        Obs.: no momento do uso deste Schema, estamos fazendo a reserva, com usuario, canoa e data. Comentario e avaliação serão submetidos em um momento posterior.
    """
    id_reserva: int = 1
    usuario: int = "21999999999"
    canoa: int = 1
    data: str = "01/05/2024" 

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
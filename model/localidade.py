from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario

class Localidade(Base):
    __tablename__ = 'locais'

    id = Column("idlocais", Integer, primary_key = True)
    estado = Column(String(2))
    municipio = Column(String(50))
    bairro = Column(String(50))
    referencia = Column(String(140))

    # Definição do relacionamento entre uma canoa e o local onde ela fica.
    # Esse relacionamento não está na tabela "locais", mas a tabela "canoas" faz uma referência à tabela locais, por meio de uma chave estrangeira.
    # O SQLAlchemy fará esse relacionamento.
    canoas = relationship("Canoas")

    def __init__(self, estado:str, municipio:str, bairro:str, referencia:str):
        """
        Cria uma localidade! As canoas ficam "hospedadas" ou "guardadas" em algum local. É nesse local que o cliente vai encontrar a canoa e passear nas águas ao seu redor.

        Arguments:
            estado: sigla do estado da federação: RJ, ES, BA etc.
            municipio
            bairro
            referencia: para dar maior clareza à localização. Exemplo: Clube dos Bombeiros, Quiosque do João etc. 
            obs.: como as canoas normalmente ficam em margens de rios, lagos, praias etc, não adianta muito atribuir um CEP.
        """
        self.estado = estado
        self.municipio = municipio
        self.bairro = bairro
        self.referencia = referencia






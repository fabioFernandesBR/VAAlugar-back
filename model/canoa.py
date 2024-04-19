from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from  model import Base


class Canoa(Base):
    __tablename__ = 'canoas'

    id = Column("idcanoas", Integer, primary_key = True)
    nome = Column(String(50))
    tipo = Column(String(20))
    dono = Column(String(50))
    telefone = Column(Integer)

    # Definição do relacionamento entre a canoa e a localidade onde está guardada ou estacionada.
    # Aqui está sendo definido a coluna 'local' que vai guardar
    # a referencia a localidade, a chave estrangeira que relaciona
    # uma canoa ao seu local.
    local = Column("idlocais", Integer, ForeignKey("locais.idlocais"), nullable=True)
    
    
    
    # Definição do relacionamento entre uma canoa e sua reserva.
    # Esse relacionamento não está na tabela "canoas", mas a tabela "reservas" faz uma referência à tabela canoas, por meio de uma chave estrangeira.
    # O SQLAlchemy fará esse relacionamento.    
    reserva = relationship("Reserva")
    

    def __init__(self, nome, tipo, dono, telefone, local, estado=None, municipio=None, bairro=None, referencia=None):
        
        # Cria uma Canoa!

        #Arguments:
        #    nome
        #    tipo
        #    dono
        #    telefone: Integer
        #    local: Integer, referência ao local onde está armazenada
        
        self.nome = nome
        self.tipo = tipo
        self.dono = dono
        self.telefone = telefone
        self.local = local

        # Atributos adicionais - para referenciar localidade
        self.estado = estado
        self.municipio = municipio
        self.bairro = bairro
        self.referencia = referencia



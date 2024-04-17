from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


from  model import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    telefone = Column(Integer, primary_key = True)
    nome = Column(String(200))
    
    # Definição do relacionamento entre uma reserva e seu usuario.
    # Esse relacionamento não está na tabela "usuarios", mas a tabela "reservas" faz uma referência à tabela usuarios, por meio de uma chave estrangeira.
    # O SQLAlchemy fará esse relacionamento.
    reserva = relationship("Reserva")

    def __init__(self, telefone, nome):
        """
        Cria um usuário! 

        Arguments:
            telefone
            nome
        """
        self.telefone = telefone
        self.nome = nome
        






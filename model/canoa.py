from sqlalchemy import Column, String, Integer, ForeignKey
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

    def __init__(self, nome, tipo, dono, telefone, local):
        """
        Cria uma Canoa!

        Arguments:
            nome
            tipo
            dono
            telefone: Integer
            local: Integer, referência ao local onde está armazenada
        """
        self.nome = nome
        self.tipo = tipo
        self.dono = dono
        self.telefone = telefone
        self.local = local
        
        
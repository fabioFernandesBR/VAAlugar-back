from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


from  model import Base


class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column("reserva", Integer, primary_key = True)
    data = Column(String(50))
    comentario = Column(String(280))
    avaliacao = Column(Integer)
    
    # Definição do relacionamento entre a reserva e a canoa que está sendo reservada.
    canoa = Column(Integer, ForeignKey("canoas.idcanoas"), nullable=False)

    # Definição do relacionamento entre a reserva e o usuario que está reservando.
    usuario = Column(Integer, ForeignKey("usuarios.telefone"), nullable=False)


    def __init__(self, usuario, canoa, data, comentario, avaliacao):
        """
        Cria uma Reserva!

        Arguments:
            canoa: referência para o id da canoa
            usuario: referência para o telefone cadastrado do usuário
            data: quando a canoa será alugada
            comentario: o que o usuario achou da experiencia
            avaliacao: nota de 1 a 5
        """
        self.usuario = usuario
        self.canoa = canoa
        self.data = data
        self.comentario = comentario
        self.avaliacao = avaliacao
        
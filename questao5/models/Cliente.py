from db import base, db
from sqlalchemy import Column, Integer, String

class Cliente(base):
    __tablename__ = "clientes"
    id_cliente = Column("id_cliente", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(90))
    estado = Column("estado", String(45))

    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado
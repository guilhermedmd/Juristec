from db import base, db
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

class Processo(base):
    __tablename__ = "processos"
    id_processo = Column("id_processo", Integer, primary_key=True, autoincrement=True)
    valor_causa = Column("valor_causa", Float)
    status = Column("status", String(45))
    assunto = Column("assunto", String(120))
    data_abertura = Column("data_abertura", Date)
    id_cliente = Column("id_cliente", ForeignKey("clientes.id_cliente"))

    def __init__(self, valor_causa, status, assunto, data_abertura, id_cliente):
        self.valor_causa = valor_causa
        self.status = status
        self.assunto = assunto
        self.data_abertura = data_abertura
        self.id_cliente = id_cliente
        
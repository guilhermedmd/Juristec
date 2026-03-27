from db import base, db
from models.Cliente import Cliente
from models.Processo import Processo

base.metadata.create_all(bind = db)
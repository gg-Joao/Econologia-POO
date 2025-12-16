from database import Database
from models.morador import Morador
from models.coleta import Coleta
from DAO import MoradorDAO, ColetaDAO
from datetime import datetime

# Cria o banco e as tabelas (opcional se DAO for em memória)
db = Database()
db.criar_tabelas()

# TESTE MORADOR
morador_dao = MoradorDAO()
morador = Morador("Carlos", "carlos@email.com", "99999999", 0, "1234")
morador_dao.inserir(morador)

print("Moradores cadastrados:")
for m in morador_dao.listar():
    print(m)

# TESTE COLETA
coleta_dao = ColetaDAO()
coleta = Coleta(None, datetime.now().isoformat(), "Coleta de papel", 10, True)
coleta_dao.inserir(coleta)

print("\nColetas cadastradas:")
for c in coleta_dao.listar():
    print(c)

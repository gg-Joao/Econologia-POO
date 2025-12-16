import sqlite3

class Database:
    def __init__(self, nome_db="sistema.db"):
        self.nome_db = nome_db

    def conectar(self):
        return sqlite3.connect(self.nome_db)

    def criar_tabelas(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS morador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
            pontos INTEGER DEFAULT 0,
            senha TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            confirmado INTEGER,
            descricao TEXT,
            pontos INTEGER
        )
        """)

        conn.commit()
        conn.close()

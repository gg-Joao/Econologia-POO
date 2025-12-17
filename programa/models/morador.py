class Morador:
    def __init__(self, nome, email, fone, pontos=0, senha=""):
        self.nome = nome
        self.email = email
        self.fone = fone
        self.pontos = pontos
        self.senha = senha

    def __str__(self):
        return f"{self.nome} ({self.pontos} pontos)"

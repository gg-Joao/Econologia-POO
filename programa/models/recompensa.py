class Recompensa:
    def __init__(self, id, nome, descricao, pontosNecessarios, tipoRecompensa, validade):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_pontos(pontosNecessarios)
        self.set_tipo(tipoRecompensa)
        self.set_validade(validade)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__pontosNecessarios} pts"

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome da recompensa é obrigatório.")
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_pontos(self, pontos):
        self.__pontosNecessarios = pontos

    def set_tipo(self, tipo):
        self.__tipoRecompensa = tipo

    def set_validade(self, validade):
        self.__validade = validade

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_pontos(self):
        return self.__pontosNecessarios

    def get_tipo(self):
        return self.__tipoRecompensa

    def get_validade(self):
        return self.__validade

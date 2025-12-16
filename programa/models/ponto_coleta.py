class PontoColeta:
    def __init__(self, id, nome, endereco, telefone, horarioFuncionamento, tipoPonto):
        self.set_id(id)
        self.set_nome(nome)
        self.set_endereco(endereco)
        self.set_telefone(telefone)
        self.set_horario(horarioFuncionamento)
        self.set_tipo(tipoPonto)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__tipoPonto}"

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome do ponto é obrigatório.")
        self.__nome = nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_horario(self, horario):
        self.__horarioFuncionamento = horario

    def set_tipo(self, tipo):
        self.__tipoPonto = tipo

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_telefone(self):
        return self.__telefone

    def get_horario(self):
        return self.__horarioFuncionamento

    def get_tipo(self):
        return self.__tipoPonto

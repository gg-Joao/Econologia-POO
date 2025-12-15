from model.operadores.usuario import Usuario

class Morador(Usuario):
    def __init__(self, nome, email, fone, senha, pontos = 0):
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_pontos(pontos)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__pontos} - {self.__senha}"
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome é obrigatório.")
        self.__nome = nome

    def set_pontos(self, pontos):
        if pontos < 0:
            raise ValueError("Não se pode ter menos de 0 pontos.")
        self.__pontos = pontos
        # pergunta ao professor: checagem de tipo é no model ou View?
    def get_nome(self):
        return self.__nome
    
    def get_pontos(self):
        return self.__pontos

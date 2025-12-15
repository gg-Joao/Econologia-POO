class Usuario:
    def __init__(self, id, tipoUsuario, email, fone, senha):
        self.set_id(id)
        self.set_tipo(tipoUsuario)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.__id} - {self.__tipo} - {self.__email} - {self.__fone}"
    
    def set_id(self, id):
        self.__id = id

    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def set_email(self, email):
        if email == "":
            raise ValueError("E-mail é obrigatório.")
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def set_senha(self, senha):
        if senha == "":
            raise ValueError("Senha é obrigatória.")
        self.__senha = senha

    def get_id(self):
        return self.__id
    
    def get_tipo(self):
        return self.__tipo

    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone
    
    def get_senha(self):
        return self.__senha
    
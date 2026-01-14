from programa.models.usuario import Usuario

class Admin(Usuario):
    def __init__(self, id=None, nome="", email="", senha=""):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)

    def __str__(self):
        return f"Admin: {self.nome}"
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
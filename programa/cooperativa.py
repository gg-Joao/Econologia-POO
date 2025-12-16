from usuario import Usuario

class Cooperativa(Usuario):
    def __init__(self, id, razaoSocial, cnpj, email, endereco, fone, senha):
        super().__init__(id, "Cooperativa", email, fone, senha)
        self.set_razao(razaoSocial)
        self.set_cnpj(cnpj)
        self.set_endereco(endereco)

    def __str__(self):
        return f"{self.get_id()} - {self.__razao} - {self.__cnpj} - {self.__endereco}"

    def set_razao(self, razao):
        if razao == "":
            raise ValueError("Razão Social é obrigatória.")
        self.__razao = razao

    def set_cnpj(self, cnpj):
        if cnpj == "":
            raise ValueError("CNPJ é obrigatório.")
        self.__cnpj = cnpj

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_razao(self):
        return self.__razao

    def get_cnpj(self):
        return self.__cnpj

    def get_endereco(self):
        return self.__endereco

class SolicitacaoRecompensa:
    def __init__(self, id, data, confirmado, item):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_item(item)

    def __str__(self):
        return f"{self.__id} - {self.__data} - Confirmado: {self.__confirmado}"

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def set_item(self, item):
        self.__item = item

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_confirmado(self):
        return self.__confirmado

    def get_item(self):
        return self.__item

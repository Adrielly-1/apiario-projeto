class Apiario():
    def __init__(self, nome_apiario, localizacao, tamanho, id_produtor):
        self._nome_apiario = nome_apiario
        self._localizacao = localizacao
        self._tamanho = tamanho
        self._id_produtor = id_produtor

    def get_nome_apiario(self):
        return self._nome_apiario

    def set_nome_apiario(self, nome_apiario):
        self._nome_apiario = nome_apiario

    def get_localizacao(self):
        return self._localizacao

    def set_localizacao(self, localizacao):
        self._localizacao = localizacao

    def get_tamanho(self):
        return self._tamanho

    def set_tamanho(self, tamanho):
        self._tamanho = tamanho

    def get_id_produtor(self):
        return self._id_produtor

    def set_id_produtor(self, id_produtor):
        self._id_produtor = id_produtor

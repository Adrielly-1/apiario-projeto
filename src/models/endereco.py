class Endereco:
    def __init__(self, logradouro, bairro, cidade, estado, cep):
        self._id_endereco = None
        self._logradouro = logradouro
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep

    #def get_id_endereco(self):
        #return self._id_endereco

    #def set_id_endereco(self, id_endereco):
        #self._id_endereco = id_endereco

    def get_logradouro(self):
        return self._logradouro

    def set_logradouro(self, logradouro):
        self._logradouro = logradouro

    def get_bairro(self):
        return self._bairro

    def set_bairro(self, bairro):
        self._bairro = bairro

    def get_cidade(self):
        return self._cidade

    def set_cidade(self, cidade):
        self._cidade = cidade

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_cep(self):
        return self._cep

    def set_cep(self, cep):
        self._cep = cep
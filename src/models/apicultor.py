class Apicultor:
    def __init__(self, nome_apicultor, endereco=None, numero=None, complemento=None, email=None, telefone=None):
        """
        Inicializa um objeto Apicultor.

        :param nome_apicultor: Nome do apicultor (obrigatório)
        :param endereco: ID do endereço (referência à tabela endereco)
        :param numero: Número do endereço
        :param complemento: Complemento do endereço
        :param email: E-mail do apicultor
        """
        self._id_apicultor = None  # Será gerado automaticamente pelo banco de dados
        self._nome_apicultor = nome_apicultor
        self._endereco = endereco
        self._numero = numero
        self._complemento = complemento
        self._email = email
        self._telefone = telefone

    # Métodos Getters e Setters

    # ID do Apicultor
    def get_id_apicultor(self):
        return self._id_apicultor

    def set_id_apicultor(self, id_apicultor):
        self._id_apicultor = id_apicultor

    # Nome do Apicultor
    def get_nome_apicultor(self):
        return self._nome_apicultor

    def set_nome_apicultor(self, nome_apicultor):
        self._nome_apicultor = nome_apicultor

    # Endereço (ID do endereço)
    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco

    # Número
    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    # Complemento
    def get_complemento(self):
        return self._complemento

    def set_complemento(self, complemento):
        self._complemento = complemento

    # E-mail
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    # Telefone
    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone
class Pessoa:
    def __init__(self, nome,  endereco, rg):
        self.nome = nome
        self.endereco = endereco
        self.rg = rg




class Bebida:
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade


class Cliente(Pessoa):
    def __init__(self, nome, endereco, rg, email, telefone, senha):
        super().__init__(nome, endereco, rg)
        self.email = email
        self.telefone = telefone
        self.senha = senha





class Gerente(Pessoa):
    def __init__(self, nome, endereco, rg, email, telefone,  senha):
        super().__init__(nome, endereco, rg)
        self.email = email
        self.telefone = telefone
        self.senha = senha






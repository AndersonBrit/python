class Pessoa:

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"O meu nome é {self.nome}, e tenho {self.idade} anos"

class Carro:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    def informação_do_carro(self):
        return f"Este é um modelo {self.marca}{self.modelo}"

pessoa = Pessoa("anderson" , 16)

print(pessoa.saudacao())
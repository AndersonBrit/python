class Atleta():

    def __init__(self, nome, idade, posicao):
        
        self.nome = nome
        self.idade = idade
        self.posicao = posicao


    def saudacao(self):
        return f"O jogador chama-se {self.nome} tem {self.idade} anos e joga na posição {self.posicao}"


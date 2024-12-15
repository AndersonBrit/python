class Atleta():

    def __init__(self, nome, idade, posicao):
        
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
    
    def __str__(self):
        return(f"Nome - {self.nome} \nIdade - {self.idade} \nPosição - {self.posicao}\n")

    def saudacao(self):
        return(f"Nome - {self.nome} \nIdade - {self.idade} \nPosição - {self.posicao}\n")
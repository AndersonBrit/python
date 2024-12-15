class Atleta():

    def __init__(self, nome, idade, posicao):
        
        self.nome = nome
        self.idade = idade
        self.posicao = posicao


    def saudacao(self):
        return f"Jogador - {self.nome} tem {self.idade} anos e joga como {self.posicao}"
    
class Equipa():

    def __init__(self, nome_equipa):

        self.nome_equipa = nome_equipa
        self.equipa = []


    def adicionar_atleta(self, pessoa):

        self.equipa.append(pessoa)


    def mostrar_equipa(self):

        for pessoa in self.equipa:
            print(pessoa)
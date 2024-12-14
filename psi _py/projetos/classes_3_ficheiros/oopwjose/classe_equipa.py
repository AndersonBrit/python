from classe_atleta import Atleta

class Equipa():

    def __init__(self, nome_equipa):

        self.nome_equipa = nome_equipa
        self.equipa = []


    def adicionar_atleta(self, pessoa):

        self.equipa.append(pessoa)


    def mostrar_equipa(self):

        for pessoa in self.equipa:
            print(pessoa)
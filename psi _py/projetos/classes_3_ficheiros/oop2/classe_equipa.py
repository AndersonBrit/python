from classe_atleta import Atleta

class Equipa ():

    def __init__(self, nome_equipa):

        self.nome_equipa = nome_equipa
        self.jogadores_equipa = []


    def mostrar_nome_equipa(self):
        return(self.nome_equipa)


    def adicionar_equipa(self, pessoa):

        self.jogadores_equipa.append(pessoa)

    def mostrar_equipa(self):

        resultado = ""

        print(f"\t{self.nome_equipa}")
        print("      Jogadores:\n\n")

        for pessoa in self.jogadores_equipa:
            resultado += str(f"{pessoa} \n")

        return resultado
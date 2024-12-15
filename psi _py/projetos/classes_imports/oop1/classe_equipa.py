from classe_atleta import Atleta

class Equipa():

    def __init__(self, nome_equipa):

        self.nome_equipa = nome_equipa
        self.equipa = []


    def adicionar_atleta(self, atleta):

        self.equipa.append(atleta)

    
    def escrever_ficheiro(self, caminho):

        with open(caminho, "w") as ficheiro:

            ficheiro.write(f"\tEquipa - {self.nome_equipa} \n\n\t Jogadores:\n\n")
            
            if not self.equipa:
                ficheiro.write("- Nenhum jogador registrado\n")
            else:
                for i in self.equipa:
                    ficheiro.write((str(i)))
                    ficheiro.write("\n")

    
    def remover_ficheiro(self, caminho):
        pass


    def mostrar_equipa(self):

        print(f"\tEquipa - {self.nome_equipa} \n\n\t Jogadores:\n\n")

        if not self.equipa:
            return(f"- Nenhum jogador registrado\n")
        
        for atleta in self.equipa:
            return(atleta)
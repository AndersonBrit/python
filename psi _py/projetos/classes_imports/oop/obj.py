from classe_atleta import Atleta
from classe_equipa import Equipa
import os
import time # colocar um tempo no if 2

def limpar_tela():

    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')


def main():

    equipas = {} # Dicionario
    caminho = r"C:\Users\dedeg\Desktop\psi _py\projetos\classes_imports\oop\obj.txt"


    while True:
        limpar_tela()
        print("\n\t=== Menu ===\n")
        print("1. Criar equipa")
        print("2. Adicionar um atleta em uma equipa")
        print("3. Mostrar equipa")
        print("4. Salvar equipa em ficheiro")
        print("5. Sair")

        
        opcao = int(input("Digite uma opção.\n"))


        if opcao == 1:

            limpar_tela()
            nome_equipa = str(input("Digite o nome da nova equipa: "))

            if nome_equipa in equipas:
                limpar_tela()
                print(f"{nome_equipa} já existe!\n")
                input("Prisone qualquer telca para continuar...")

            else:
                limpar_tela()
                equipas[nome_equipa] = Equipa(nome_equipa)
                print(f"Equipa '{nome_equipa}' criada com sucesso!\n")
                input("Prisone qualquer telca para continuar...")
        

        elif opcao == 2:

            limpar_tela()

            if not equipas:
                print("Nenhuma equipa existente. Crie uma equipa.\n")
                input("Prisone qualquer telca para continuar...")

            else:
                nome_equipa = str(input("Digite o nome da equipa: "))

                if nome_equipa not in equipas:
                    limpar_tela()
                    print("Equipa não encontrada!\n")
                    input("Prisone qualquer telca para continuar...")

                else:
                    limpar_tela()
                    print(f"Inserir dados do atleta da equipa {nome_equipa}\n")
                    nome = str(input("Nome do atleta: "))
                    idade = int(int(input("Idade do atleta: ")))
                    posicao = str(input("Posição do atleta: "))

                    atleta = Atleta(nome, idade, posicao)

                    equipas[nome_equipa].adicionar_atleta(atleta)
                    
                    limpar_tela()
                    print(f"Atleta '{nome}' adicionado à equipa '{nome_equipa}'!\n")
                    input("Prisone qualquer telca para continuar...")
        

        elif opcao == 3:

            limpar_tela()

            if not equipas:
                print("Nenhuma equipa existente.\n")
                input("Prisone qualquer telca para continuar...")

            else:
                for nome, equipa in equipas.items():
                    equipa.mostrar_equipa()

                input("Prisone qualquer telca para continuar...")
        

        elif opcao == 4:

            limpar_tela()
            nome_equipa = str(input("Digite o nome da equipa que quer salvar: "))

            if nome_equipa not in equipas:
                limpar_tela()
                print("Equipa não existente\n")
                input("Prisone qualquer telca para continuar...")

            else:
                limpar_tela()
                #pedir ao utilizador o caminho do ficheiro
                equipas[nome_equipa].escrever_ficheiro(caminho)
                print(f"Dados da equipa '{nome_equipa}' salvos em '{caminho}'!\n")
                input("Prisone qualquer telca para continuar...")


        elif opcao == 5:
            limpar_tela()
            print("Programa encerrado")
            input("Prisone qualquer telca para continuar...")
            break


        else:
            limpar_tela()
            print("Opção inválida. Tente novamente.")


main()
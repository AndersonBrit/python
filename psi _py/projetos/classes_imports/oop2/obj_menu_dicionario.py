from classe_atleta import Atleta
from classe_equipa import Equipa
import os

def limpar_tela():
    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')

def menu():

    equipas = {}

    while True:
        limpar_tela()
        print("\n\t=== Menu ===\n")
        print("1. Criar equipa") #colocar em um diconario para poder alternar entre equipas
        print("2. Adicionar um atleta em uma equipa") #poder escolher equipa que quero adicionar
        #fazer a media das idades
        print("3. Mostrar equipa") #poder escolher equipa que quero adicionar
        print("4. Salvar equipa em ficheiro") #poder escolher equipa que quero adicionar
        print("5. Sair\n") #colocar os "..." para aparecer um de cada vez e desaparecer e voltar a aperecer um de cada vez

        opcao = str(input("Digite uma opcao valida\n"))

        if opcao == "1":

            limpar_tela()
            nome_equipa = str(input("Qual nome desejado para a equipa\n"))
            nome_equipa = Equipa(nome_equipa)

            limpar_tela()
            print(f"Nome da equipa defenido como - {nome_equipa.mostrar_nome_equipa()}")
            input("Presione qualquer tecla para continuar ...")

        if opcao == "2":

            limpar_tela()

            if not nome_equipa:
                print("Cire primeiro uma equipa")
                input("Presione qualquer tecla para continuar ...")
                continue

            limpar_tela()
            nome = str(input("Digite o nome do jogador\n"))
            limpar_tela()
            idade = int(input("Digite a idade do jogador\n"))
            limpar_tela()
            posicao = str(input("Digite a posição do jogador\n"))


            limpar_tela()
            jogador = Atleta(nome, idade, posicao)
            nome_equipa.adicionar_equipa(jogador)
            print(f"Jogador acicionado com sucesso:\n\n{jogador.saudacao()}\n")
            input("Presione qualquer tecla para continuar ...")

        if opcao == "3":

            limpar_tela()

            if not nome_equipa:
                print("Cire primeiro uma equipa")
                input("Presione qualquer tecla para continuar ...")
                continue
        
            limpar_tela()
            print(nome_equipa.mostrar_equipa())
            input("Presione qualquer tecla para continuar ...")


        if opcao == "5":

            limpar_tela()
            print("Programa encerrado")
            break

menu()
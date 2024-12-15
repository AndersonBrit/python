import os
import time


def limpar_tela():


    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')


def vscode():
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")


def google():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")


def abrir_n_vezes(func, n=1):

    for _ in range(n):

        func()
        limpar_tela()

    print("Operação feita")
    time.sleep(2)


def iniciar():

    while True:

        limpar_tela()

        print("\nEscolha uma opção:")
        print("1 - Abrir VSCode 1 vez")
        print("2 - Abrir VSCode 2 vezes")
        print("3 - Abrir Google 1 vez")
        print("4 - Abrir Google 2 vezes")
        print("5 - Abrir VSCode e Google 1 vez")
        print("6 - Abrir VSCode e Google 2 vezes")
        print("7 - Sair do programa")

        num1 = int(input())

        if num1 == 1:
            abrir_n_vezes(vscode)


        elif num1 == 2:
            abrir_n_vezes(vscode, 2)


        elif num1 == 3:
            abrir_n_vezes(google)
            limpar_tela()


        elif num1 == 4:
            abrir_n_vezes(google, 2)


        elif num1 == 5:
            abrir_n_vezes(vscode)
            abrir_n_vezes(google)
            limpar_tela()


        elif num1 == 6:
            abrir_n_vezes(vscode, 2)
            abrir_n_vezes(google, 2)


        elif num1 == 7:
            limpar_tela()
            print("Programa encerrado")
            break


        else:
            print("Opção errada")
            time.sleep(2)
            limpar_tela()


iniciar()
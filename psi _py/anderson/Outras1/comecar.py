import os


def limpar_tela():


    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')


def vscode():
    os.startfile(r"C:\Users\dedeg\Desktop\Visual Studio Code.lnk")


def google():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")


def abrir_n_vezes(func, n=1):

    for _ in range(n):

        func()
        limpar_tela()


def iniciar():

    while True:

        limpar_tela()

        num1 = int(input())

        if num1 == 1:
            abrir_n_vezes(vscode)
            break


        elif num1 == 2:
            abrir_n_vezes(vscode, 2)
            break


        elif num1 == 3:
            abrir_n_vezes(google)
            limpar_tela()
            break


        elif num1 == 4:
            abrir_n_vezes(google, 2)
            break


        elif num1 == 5:
            abrir_n_vezes(vscode)
            abrir_n_vezes(google)
            limpar_tela()
            break


        elif num1 == 6:
            abrir_n_vezes(vscode, 2)
            abrir_n_vezes(google, 2)
            break


        else:
            limpar_tela()


iniciar()
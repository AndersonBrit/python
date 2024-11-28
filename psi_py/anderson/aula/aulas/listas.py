import os

def limpar_tela():

    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')


lista = [1,(2),"3",[4]]

def Lista():

    limpar_tela()
    print(lista)

Lista()
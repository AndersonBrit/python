import os

def limpar_tela():

    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')

class Pessoa:
    
    def __init__(self, nome, idade): 

        self.nome = nome
        self.idade = idade

    def apresentar(self):
        
        print(f"Bem vindo {self.nome}, voce tem {self.idade} anos")


lista_pessoas = []

while True:

    limpar_tela()
    menu = int(input("1 - Inserir dados \n2 - Ver lista dos dados \n3 - Sair\n"))

    if menu == 1:

        limpar_tela()
        var_repeticao = int(input("Quantas pessoas quer adicionar\n"))
        num1 = 1

        for _ in range(var_repeticao):

            limpar_tela()

            print(f"[{num1}/{var_repeticao}]")
            nome = str(input("Digite o nome desejado\n"))
            idade = str(input("\nDigite a idade desejada\n"))

            limpar_tela()
            pessoa = Pessoa(nome, idade)
            lista_pessoas.append(pessoa)
            
            print(f"[{num1}/{var_repeticao}]")
            print("Pessoa adicionada com sucesso!")
            input("\nPressione Enter para continuar...")
            num1 += 1


    elif menu == 2:

        limpar_tela()

        if not lista_pessoas:
            print("Lista vazia")

        else:
            print("Lista de pessoas\n")

            for i, pessoa in enumerate(lista_pessoas, start=1):
                print(f"{i}. Nome: {pessoa.nome}, Idade: {pessoa.idade} anos")


        input("\nPressione Enter para continuar...")

    elif menu == 3:

        limpar_tela()
        print("Programa encerrado")
        break


    else:

        limpar_tela()
        print("Opção errada")
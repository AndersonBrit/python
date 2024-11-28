import time

def limpar_tela():
    """Limpa a tela para melhorar a jogabilidade."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def remate(jogador, adversario, opcoes_remate):
    """Executa um remate e verifica o resultado."""
    limpar_tela()
    print(f"Turno de {jogador} para chutar!")
    
    print("\nEscolha seu remate:")
    for i, opcao in enumerate(opcoes_remate, start=1):
        print(f"{i} - {opcao}")
    
    chute = int(input(f"{jogador}, digite o número do seu remate: "))
    while chute < 1 or chute > 5:
        print("Escolha inválida. Tente novamente.")
        chute = int(input(f"{jogador}, digite o número do seu remate: "))
    
    limpar_tela()
    print(f"{adversario}, escolha onde defender!")
    for i, opcao in enumerate(opcoes_remate, start=1):
        print(f"{i} - {opcao}")
    
    defesa = int(input(f"{adversario}, digite o número do local de defesa: "))
    while defesa < 1 or defesa > 5:
        print("Escolha inválida. Tente novamente.")
        defesa = int(input(f"{adversario}, digite o número do local de defesa: "))
    
    return chute, defesa

def main():
    limpar_tela()
    print("Bem-vindo ao desafio de pênaltis 1 contra 1!")
    
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")
    
    opcoes_remate = [
        "Canto inferior esquerdo",
        "Canto inferior direito",
        "Canto superior esquerdo",
        "Canto superior direito",
        "Meio"
    ]
    
    gols_jogador1 = 0
    gols_jogador2 = 0
    
    for rodada in range(1, 6):
        print(f"\n=== Rodada {rodada} ===")
        
        # Turno do Jogador 1
        chute, defesa = remate(jogador1, jogador2, opcoes_remate)
        if chute == defesa:
            print(f"{jogador2} DEFENDEU o remate de {jogador1}!")
        else:
            print(f"GOOOOL de {jogador1}!")
            gols_jogador1 += 1
        time.sleep(2)
        
        # Turno do Jogador 2
        chute, defesa = remate(jogador2, jogador1, opcoes_remate)
        if chute == defesa:
            print(f"{jogador1} DEFENDEU o remate de {jogador2}!")
        else:
            print(f"GOOOOL de {jogador2}!")
            gols_jogador2 += 1
        time.sleep(2)
    
    # Resultado final
    limpar_tela()
    print("\n=== Fim do Jogo! ===")
    print(f"{jogador1} marcou {gols_jogador1} gol(s).")
    print(f"{jogador2} marcou {gols_jogador2} gol(s).")
    
    if gols_jogador1 > gols_jogador2:
        print(f"\nParabéns, {jogador1}! Você venceu!")
    elif gols_jogador2 > gols_jogador1:
        print(f"\nParabéns, {jogador2}! Você venceu!")
    else:
        print("\nO jogo terminou EMPATADO!")

if __name__ == "__main__":
    main()

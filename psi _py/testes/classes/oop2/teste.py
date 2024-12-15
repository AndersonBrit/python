from classe_atleta import Atleta
from classe_equipa import Equipa

# Dicionário para armazenar equipas
equipas = {}

# Adicionar uma nova equipa
nome_equipa = "Cova" 
nova_equipa = Equipa(nome_equipa) 
equipas[nome_equipa] = nova_equipa

nome_equipa2 = "cova2"
nova_equipa2 = Equipa(nome_equipa2)
equipas[nome_equipa2] = nova_equipa2

# Listar todas as equipas
for nome, equipa in equipas.items():
    print(f"Nome da equipa: {nome}")

# Alternar para uma equipa específica
nome_escolhido = input("Digite o nome da equipa desejada: ")
equipa_atual = equipas.get(nome_escolhido)

# Trabalhar na equipa selecionada
if equipa_atual:
    print(f"Equipa selecionada: {equipa_atual.nome_equipa}")
else:
    print("Equipa não encontrada.")

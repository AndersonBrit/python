from classe_atleta import Atleta
from classe_equipa import Equipa

caminho = r"C:\Users\dedeg\Desktop\psi _py\projetos\classes_imports\oop\obj.txt"

pessoa1 = Atleta("Silva", 16, "Ala")
pessoa2 = Atleta("Jose", 18, "Central")
equipa1 = Equipa("Cova")

equipa1.adicionar_atleta(pessoa1)
equipa1.adicionar_atleta(pessoa2)

print(equipa1.mostrar_equipa())
from classe_atleta import Atleta
from classe_equipa import Equipa


pessoa1 = Atleta ("silva",16,"ALA/fixo")                          

pessoa2 = Atleta ("piri", 17, "Pivo")

pessoa3 = Atleta ("José", 17, "Ala/fixo/pivo")

pessoa4 = Atleta ("Anderson", 16, "Guarda-redes")

pessoa5 = Atleta ("Edu", 16, "ALA/fixo")

pessoa6 = Atleta ("Rosa", 17, "Fixo")

pessoa7 = Atleta ("Leonardo", 16, "Guarda Redes")

pessoa8 = Atleta ("Almeida", 16, "Ala/fixo")

pessoa9 = Atleta ("Gustavo Matos", 17, "ALA")

pessoa10 = Atleta ("Apolinario", 16, "ALA")

pessoa11 = Atleta ("Coelho", 16, "FIXO")

pessoa12 = Atleta ("Lino", 17,"Treinador")


equipa1 = Equipa("11º GPSI")    

equipa1.adicionar_atleta(pessoa1)
print(equipa1.mostrar_equipa)

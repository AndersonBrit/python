from classe_atleta import Atleta
from classe_equipa import Equipa


pessoa1 = Atleta ("silva",16,"ALA/fixo")
print(pessoa1.saudacao())                            #funcao da dentro da variavel pessoa

pessoa2 = Atleta ("piri", 17, "Pivo")
print(pessoa2.saudacao())

pessoa3 = Atleta ("José", 17, "Ala/fixo/pivo")
print(pessoa3.saudacao())

pessoa4 = Atleta ("Anderson", 16, "Guarda-redes")
print(pessoa4.saudacao())

pessoa5 = Atleta ("Edu", 16, "ALA/fixo")
print(pessoa5.saudacao())

pessoa6 = Atleta ("Rosa", 17, "Fixo")
print(pessoa6.saudacao())

pessoa7 = Atleta ("Leonardo", 16, "Guarda Redes")
print(pessoa7.saudacao())

pessoa8 = Atleta ("Almeida", 16, "Ala/fixo")
print(pessoa8.saudacao())

pessoa9 = Atleta ("Gustavo Matos", 17, "ALA")
print(pessoa9.saudacao())

pessoa10 = Atleta ("Apolinario", 16, "ALA")
print(pessoa10.saudacao())

pessoa11 = Atleta ("Coelho", 16, "FIXO")
print(pessoa11.saudacao())

pessoa12 = Atleta ("Lino", 17,"Treinador")
print(pessoa12.saudacao())


equipa1 = Equipa("11º GPSI")    

equipa1.adicionar_atleta(pessoa1)
print(equipa1.mostrar_equipa)

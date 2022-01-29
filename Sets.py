#  Coleção desodernada, imutável e não permite valores duplicados.
#  Também conhecidos como conjuntos.

conj = {"item1", "item2", "item3"}
print(conj)
print(type(conj))
print(len(conj))

tupla = (3, 7, 5, 4)
conj1 = set(tupla)
print(conj1)
print(type(conj1))
print(7 in conj1)

print(50*"-")

conjunto = {"item1", "item2", "item3"}

for x in conjunto:
    print(x)

conjunto.add("item4")  # função para adicionar elementos
conjunto.add(10)
conjunto.add(False)
print(conjunto)
conjunto.pop()  # remove um item aleatório do set
conjunto.remove("item2")  # remove um item selecionado no set
conjunto.discard("item6")  # remove também, mas não dá erro caso não encontre
print(50*"-")

set1 = {1, 2, 7, 5, 8}
set2 = {1, 4, 8, 7, 10}
set3 = set1.union(set2)  # define a unão dos dois conjuntos, sem repetir
set4 = set1.intersection(set2)  # define os números repetidos entre os dois
set5 = set1.symmetric_difference(set2)  # define os números que se diferem
print(set3)  # união
print(set4)  # repetidos
print(set5)  # diferentes

#  Coleção desodernada, imutável e não permite valores duplicados.
#  Também conhecidos como conjuntos.

"""conj = {"item1", "item2", "item3"}
print(conj)
print(type(conj))
print(len(conj))"""

tupla = (3, 7, 5, 4)
conj = set(tupla)
print(conj)
print(type(conj))
print(7 in conj)

conjunto = {"item1", "item2", "item3"}

for x in conjunto:
    print(x)

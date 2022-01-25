tupla = ("item1", "item2", "item3", "item1", "item1")
print(tupla)
print(len(tupla))
print(type(tupla))

print(tupla.count("item3"))

uf = ("RN", "PE", "CE", "PB", "AL", "BA")
print(type(uf))
print("--------------------------------")
tupla1 = ("uva", "maçã", "banana", "morango")
print(tupla1)

for x in range(len(tupla1)):  # o loop funciona parecido com Listas
    print(x, tupla1[x])

(x, *y, z) = tupla1  # desempacotamento de uma Tupla
print("x:", x)
print("y:", y)
print("z:", z)

# Tuplas são mais utilizados em coisas que não devem ser mudadas,
# como os estados brasileiros (exemplo acima).

# É um coleção bem parecida com Listas, porém, são imutáveis.
# Isto é, não há muitas funções, como append, insert, pop etc.

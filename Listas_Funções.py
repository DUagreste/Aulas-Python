# Aprendendo listas + funções

"""print("-----------------------------------")
lista1 = [2.0, 3.5, 7.5, -2, 12, 25]
print(lista1)
print(len(lista1))  # tamanho da lista
print(sum(lista1))  # somatório da lista
print(max(lista1))  # o maior número da lista
print(min(lista1))  # o menor número da lista

nome = "Vitor"
valor = range(10)

lista2 = list(range(10))
print(lista2)

lista3 = list(nome)
print(lista3)

elemento = 8

if elemento in lista2:
    print("Este elemento está dentro da lista!")

print(type(lista3))"""

print("-----------------------------------")
lista4 = ["bulls", "lakers", "nets"]
print(lista4)
lista4[0] = "spurs"
print(lista4)
lista4[1:3] = ["heat", "mavericks"]
print(lista4)
lista4[2:3] = ["thunder", "jazz"]
print(lista4)
print("-----------------------------------")

lista4.append("raptors")   # adiciona 1 elemento ao final da lista
print(lista4)

lista4.insert(1, "hawks")   # insere um elemento no index selecionado
print(lista4)

lista4.extend(["warriors", "cavaliers"])   # adiciona uma lista de elementos
print(lista4)

lista4.pop(4)   # remove o elemento no index designado
print(lista4)

lista4.remove("thunder")   # remove o elemento citado
print(lista4)

del lista4[2]   # apaga o elemento no index designado/ou apaga a lista [vazio]
print(lista4)

lista4.sort()   # ordena os elementos em ordem alfabética/crescente
print(lista4)

"""Pode-se usar >lista4.sort(key = str.lower)< caso queria destinguir
maiúsculo de minúsculo e assim ordernar corretamente"""

lista4.reverse()   # reverte os elementos da lista
print(lista4)

lista4.clear()   # limpa os elementos da lista
print(lista4)

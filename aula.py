# Aprendendo listas

lista1 = [2.0, 3.5, 7.5, -2, 12, 25]
print(lista1)
print(len(lista1))
print(sum(lista1))
print(max(lista1))
print(min(lista1))

nome = "Vitor"
valor = range(10)

lista2 = list(range(10))
print(lista2)

lista3 = list(nome)
print(lista3)

elemento = 8

if elemento in lista2:
    print("Este elemento está dentro da lista!")

print(type(lista3))


lista4 = ["gato", "cachorro", "peixe", "leão", "tigre"]
print(lista4)
lista4[0] = "ave"
print(lista4)
lista4[1:4] = ["girafa", "morcego", "elefante"]
print(lista4)
lista4[4:5] = ["aranha", "cobra"]
print(lista4)

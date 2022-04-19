# Programa que pede um nome ao usuário. Irá responder o tamanho
# baseado no número de caracteres digitado.

nome = input("Digite um nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print(f"{nome} é um nome curto!")
elif tamanho <= 6:
    print(f"{nome} é um nome médio!")
elif tamanho <= 10:
    print(f"{nome} é um nome grande!")
else:
    print(f"{nome} é um nome enorme!")

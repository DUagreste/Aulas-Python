# Descobrir número é par ou impar

print("-----------------------------")

numero = input("Digite um número: ")

if numero.isnumeric():
    numero = int(numero)

    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é impar!.")
else:
    print("Digite um número válido!")

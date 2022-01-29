# Descobrir fatorial de um número
print("------------------------------")
numero = int(input("Digite um número: "))

fatorial = 1

if numero < 0:
    print("Não existe fatorial de número negativo!")
elif numero == 0:
    print("O fatorial de 0 é 1!")
else:
    for x in range(1, numero+1):
        fatorial = fatorial * x
    print(f"O fatorial de {numero} é: {fatorial}")

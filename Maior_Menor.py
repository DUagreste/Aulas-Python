# Exercício: descubra o maior e menor número

cont = 0

while cont < 5:
    numero = int(input("Digite o número: "))
    if cont == 0:
        menor = numero
        maior = numero
    if numero > maior:
        maior = numero
    elif menor > numero:
        menor = numero
    cont = cont + 1

print(f"O maior número é {maior} e menor é {menor}")

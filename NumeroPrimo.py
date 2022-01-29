# Verificar se o número é primo

print("------------------------")

numero = int(input("Digite um número: "))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Não é um número primo!")
            break
    else:
        print("O número é primo!")
else:
    print("Número inválido!")

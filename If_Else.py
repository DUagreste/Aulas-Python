print("----------------------------")
# Exercício 01

idade = int(input("Qual sua idade? "))

if (idade < 16):
    print("Você é de menor!")
elif (16 >= idade or idade <= 18):
    print("Você é um emancipado!")
else:
    print("Você é de maior!")

print("----------------------------")
# Exercício 02

nadador = int(input("Qual a idade do nadador? "))

if (nadador >= 5 and nadador <= 7):
    print("Sua categoria é Infantil A.")
if (nadador >= 8 and nadador <= 10):
    print("Sua categoria é Infantil B.")
if (nadador >= 11 and nadador <= 13):
    print("Sua categoria é Juvenil A.")
if (nadador >= 14 and nadador <= 17):
    print("Sua categoria é Juvenil B.")
if (nadador < 5 or nadador > 17):
    print("Idade fora dos padrões.")

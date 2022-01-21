# Exercício 01 - Área do retângulo

print("Calcule a área do retângulo (em m²)")

base = input("Qual o tamanho da base do retângulo? ")
altura = input("Qual o tamanho da altura do retângulo? ")
area = float(base) * float(altura)

print(f'O seu retângulo possui área de {area} m².')

print("------------------------------------------------")
# Exercício 02 - Área do quadrado

print("Calcule a área do quadrado (em cm²)")

base2 = input("Qual o tamanho da base do quadrado? ")
altura2 = input("Qual o tamanho da altura do quadrado? ")
area2 = float(base2) * float(altura2)

print(f'O quadrado tem {area2} cm².')

print("------------------------------------------------")
# Exercício 03 - Cálculo de desconto

print("Calcule o desconto do produto")

produto = float(input("Qual o valor do produto? R$"))
desconto = float(input("Qual o desconto? "))
desconto = desconto/100

print("O valor do produto com desconto ficou R$", produto * (1-desconto))

print("------------------------------------------------")
# Exercício 04 - Área do círculo

print("Calcule a área do círculo (em m²)")

raio = float(input("Qual o tamanho do raio círculo? "))
pi = 3.14
area = pi * (raio ** 2)

print(f'O tamanho do círculo é {area} m².')

print("------------------------------------------------")
# Exercício 04 - Conversão de dinheiro

print("Conversão de reais para dólares")

real = float(input("Quantos reais quer converter? R$"))
convertReal = real / 5.52

print(f'A quantia em dólares é US${convertReal:.2f}.')
print("------------------------------------------------")
print("Conversão de dólares para reais")

dolar = float(input("Quantos dólares quer convertes? US$"))
convertDolar = dolar * 5.52

print(f'A quantia em dólares é R${convertDolar:.2f}.')

print("-----------------------------")

# Questão 02

chances = list()
contador = int(input("Insira quantos elementos deseja acrescentar: "))
for i in range(1, contador+1):
    chances.append(int(input("Digite o número: ")))
    contador += 1
print(chances)

# Nessa questão eu não fui muito bem, teria que multiplicar os elementos
# todos por 3, e eu ainda não sei como faria isso.

print("-----------------------------")

# Questão 03

frase = input("Escreva uma frase: ")
letra = input("Selecione uma letra: ")

print(f"A letra selecionada aparece {frase.count(letra)} vez(es)")

# Essa foi a mais fácil, já que o Python já tem uma função adequada.
# No processo seletivo deixei até mais simples.

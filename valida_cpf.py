# Programa que valida CPF, baseando-se nos dois últimos dígitos.

while True:
    cpf = input("Digite o CPF para validação [sem pontuação]: ")
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)

    if cpf == novo_cpf:
        print('CPF VÁLIDO!')
    else:
        print('CPF INVÁLIDO')

# Programa que valida CPF, baseando-se nos dois últimos dígitos.

while True:    # Loop infinito
    cpf = input("Digite o CPF para validação [sem pontuação]: ")
    novo_cpf = cpf[:-2]    # Elimina os dois últimos dígitos do CPF
    reverso = 10    # Contador reverso
    total = 0

    for index in range(19):
        if index > 8:    # Primeiro índice vai de 0 a 9
            index -= 9    # São os 9 primeiros dígitos do CPF

        total += int(novo_cpf[index]) * reverso    # Valor total

        reverso -= 1    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:    # Se o dígito for > 9, o valor é 0
                digito = 0
            total = 0    # Zera o total
            novo_cpf += str(digito)    # Concatena o dígito gerado pelo cpf

    # Para evitar que sequências sejam validadas
    sequencia = novo_cpf == str(novo_cpf[0]) * 11

    if cpf == novo_cpf and not sequencia:
        print('CPF VÁLIDO!')
    else:
        print('CPF INVÁLIDO')

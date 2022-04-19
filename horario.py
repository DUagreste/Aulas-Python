# Um programa que responde uma saudação dependendo do horário
# digitado pelo usuário.

hora = input("Digite um horário [0-24]: ")

if hora.isnumeric():
    hora = int(hora)

    if hora > 24:
        print("O horário tem de estar entre 0 e 24!")
    else:
        if hora >= 4 and hora <= 11:
            print("Bom dia!")
        elif hora >= 12 and hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
else:
    print("Digite com números válidos!")

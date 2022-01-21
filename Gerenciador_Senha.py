'''
Security = chave
5ecur1ty = senha
'''


chave = input("Digite sua senha: ")
senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "@"
    elif letra in "Bb":
        senha = senha + "1"
    elif letra in "Cc":
        senha = senha + "2"
    elif letra in "Dd":
        senha = senha + "3"
    elif letra in "Ee":
        senha = senha + "&"
    elif letra in "Ff":
        senha = senha + "7"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "$"
    elif letra in "Ii":
        senha = senha + "!"
    else:
        senha = senha + letra
print(senha)

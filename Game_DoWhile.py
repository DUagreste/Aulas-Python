# Mini game - Acerte o número

palpite = 0
numero = 9

while True:
    print("---------------------------")
    print("Advinhe o número!")
    palpite = int(input("Dê seu palpite: "))
    if palpite == numero:
        print("Parabéns, você acertou!")
        break
    else:
        print("Que pena, você errou!")

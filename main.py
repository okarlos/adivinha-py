print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")

numero_secreto: int = 42
chute: int = 1
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("*********************************")
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("O número secreto está entre 1 e 100!")
        continue

    if numero_secreto == chute:
        print("Você acertou! O número secreto é", numero_secreto, "!")
        break
    else:
        if numero_secreto > chute:
            print("Errou! O número secreto é maior que", chute, ".")
        elif numero_secreto < chute:
            print("Errou! O número secreto é menor que", chute, ".")
print("Fim do jogo")

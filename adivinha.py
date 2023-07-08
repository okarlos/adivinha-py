import random

print("**********************************************************")
print("************Bem-vindo ao jogo de Adivinhação!*************")
print("**********************************************************")
print("Você começa o jogo com 200 pontos.")
print("A cada chute incorreto você perde pontos igual a diferença.")
print("Se ficar sem pontos ou sem tentativas, o jogo acaba!")
print("Boa sorte!! =)")
print("**********************************************************")
numero_secreto: int = random.randrange(1,101)
pontos = 200 #pontuação inicial

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#print(numero_secreto)

for rodada in range(1,total_de_tentativas + 1):
    print("*********************************")
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("O número secreto está entre 1 e 100!")
        continue

    if numero_secreto == chute:
        print("Você acertou! O número secreto é {}! Você fez {} pontos!".format(numero_secreto, pontos))
        break
    else:
        if numero_secreto > chute:
            print("Errou! O número secreto é maior que", chute, ".")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        elif numero_secreto < chute:
            print("Errou! O número secreto é menor que", chute, ".")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        pontos_perdidos = abs(numero_secreto-chute)
        pontos = (pontos - pontos_perdidos)
        if pontos <= 0:
            pontos = 0
            print("O jogo acabou! Você não tem mais pontos disponíveis!")
            break

print("Fim do jogo")

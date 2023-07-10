def jogar():
    print("**********************************************************")
    print("***************Bem-vindo ao jogo de Forca!****************")
    print("**********************************************************")

    palavra_secreta = "teste"
    acertos = ["_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(acertos)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                acertos[index] = letra
            index = index + 1
        print(acertos)


if(__name__ == "__main__"):
    jogar()
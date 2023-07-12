def jogar():
    print("**********************************************************")
    print("***************Bem-vindo ao jogo de Forca!****************")
    print("**********************************************************")

    palavra_secreta = "karlos".upper()
    acertos = ["_" for letra in palavra_secreta] #cria uma lista com o mesmo tamanho de palavra_secreta

    enforcou = False
    acertou = False
    erros = 0

    print("")
    print(acertos)
    print("")

    while(not enforcou and not acertou):

        print("Você tem {} tentativa(s).".format(len(palavra_secreta)-erros)) #tentativas = tamanho da palavra secreta menos os erros
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    acertos[index] = letra
                index += 1 #mesma saída de index = index + 1
        else:
            erros += 1

        enforcou = erros == len(palavra_secreta) #permite N erros, onde N é igual ao número de letras da palavra secreta
        acertou = "_" not in acertos #valida se tem algum _ em acertos, se não tiver é porque a palavra foi descoberta
        print(acertos)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Vocês perdeu!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
import random

def jogar():
    mensagem_boas_vindas()

    palavra_secreta = sorteia_palavra_secreta()
    
    acertos = ["_" for letra in palavra_secreta] #cria uma lista com o mesmo tamanho de palavra_secreta

    enforcou = False
    erros = 0

    print("\n", acertos, "\n")

    while not enforcou and "_" in acertos:

        #tentativas = tamanho da palavra secreta menos os erros
        print("Você tem {} tentativa(s).".format(len(palavra_secreta)-erros))
        chute = input("Digite uma letra: ").upper().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra válida.")
            continue

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, acertos)
        else:
            erros += 1

        #permite N erros, onde N é igual ao número de letras da palavra secreta
        enforcou = erros == len(palavra_secreta) 

        #valida se tem algum _ em acertos, se não tiver é porque a palavra foi descoberta
        print(acertos)

    if "_" not in acertos:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

def mensagem_boas_vindas():
    print("**********************************************************")
    print("***************Bem-vindo ao jogo de Forca!****************")
    print("**********************************************************")

def sorteia_palavra_secreta():
    with open("palavras.txt") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

    index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[index].upper()
    return palavra_secreta

def marca_chute_correto(chute, palavra_secreta, acertos):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            acertos[index] = letra
        index += 1 #mesma saída de index = index + 1

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Vocês perdeu! A palavra era {}.".format(palavra_secreta))

if(__name__ == "__main__"):
    jogar()
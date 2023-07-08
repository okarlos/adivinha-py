import forca
import adivinha

def escolhe_jogo():
    print("**********************************************************")
    print("*******************Escolha o seu jogo!********************")
    print("**********************************************************")

    print("(1) Adivinhação (2) Forca")
    jogo = int(input("Qual jogo quer jogar?"))

    if jogo == 1:
        print("Iniciando Adivinhação...")
        adivinha.jogar()
    elif jogo == 2:
        print("Iniciando Forca...")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
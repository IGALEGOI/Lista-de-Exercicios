from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

def obterNota(entrada):

    ret = False

    while not ret:

        if entrada == 1 or entrada == 2:
            texto = "[NP" + str(entrada) + "]"
        else:
            texto = "EXAME"

        nota    = float(input("Informe nota da " + texto + ": "))

        ret = validaNota(nota)

    return nota

def validaNota(entrada):

    if entrada > -1 and entrada < 11:
        ret = True 
    else: 
        ret = False

    if not ret:
        print("Valor inválido!! Informe uma nota entre 0 e 10!")

    return ret

def situacaoPadrao(entrada):
    if entrada >= 7:
        saida = "APROVADO!"
    elif (entrada < 3):
        saida = "REPROVADO!"
    else:
        saida = "EXAME!"
    
    return saida

def situacaoExame(entrada):
    if entrada >= 5:
        saida = "APROVADO!"
    else:
        saida = "REPROVADO!"
    
    return saida    

continua = "S"
while continua == "S" or continua == "s":

    clear()

    np1 = obterNota(1)
    np2 = obterNota(2)

    media = (np1 + np2)/2

    textoSituacao = "O aluno "
    textoSituacao += "ficou de EXAME!" if situacaoPadrao(media) == "EXAME!" else "foi " + str(situacaoPadrao(media))

    print(textoSituacao)

    if situacaoPadrao(media) == "EXAME!":
        exame = obterNota(0)

        mediaExame = (media + exame)/2

        print("O aluno foi " + str(situacaoExame(mediaExame)))

    continua = input("\nDeseja informar outro número? [S/N] ")

    clear()
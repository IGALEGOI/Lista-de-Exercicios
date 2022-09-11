from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

def obterNumero():

    ret = False
    while not ret:
        var = int(input("Informe um número inteiro: "))
        ret = validacao(var)
    
    return var

def validacao(entrada):

    if(entrada < 0):
        print("Este número é negativo! Informe um número valido!")

    return entrada >= 0

def parImpar(entrada):

    if entrada % 2 == 0:
        print("Este número é PAR!")
    else:
        print("Este número é IMPAR!") 

continua = "S"
while continua == "S" or continua == "s":

    clear()

    numeroInteiro = obterNumero()
    parImpar(numeroInteiro)
    continua = input("\nDeseja informar outro número? [S/N] ")

    clear()
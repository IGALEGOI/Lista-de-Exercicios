from xmlrpc.client import boolean
from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

def validacaoEntrada(entrada):
    ret = boolean(False if entrada < 0 else True)
    if not ret: 
        print("Informe um valor valido!")
    return ret 

def validacaoPontos(primeiraEntrada, segundaEntrada):
    ret = boolean(False if primeiraEntrada > segundaEntrada else True)
    if not ret: 
        print("O primeiro ponto é maior que o segundo! Informe novamente os pontos!")
    return ret

def obterDados(entrada):
    ret = False
    while not ret:
        variavel = float(input(entrada)) 
        ret = validacaoEntrada(variavel)
    return variavel

def resultado(entradaPontoUm, entradaPontoDois, entradaTempo):
    return (entradaPontoDois - entradaPontoUm) / entradaTempo

def conversor(entradaValor):
    ret = False
    while not ret:
        metragem = input("Por favor, informe a qual a metragem informado, se foi m/s = (S) ou km/h = (H): ")
        if (metragem == "S" or metragem == "s") or (metragem == "H" or metragem == "h"): 
            ret = True
        else: 
            ret = False

    if metragem == "S" or metragem == "s":
       return entradaValor * 3.6
    else:
       return entradaValor 

def validaMulta(entrada):
    if entrada > 100:
        return " Ultrapassando o limite de 100 Km/h, o condutor será multado por excesso de velocidade na via!"
    else:
        return ""

ret = False
while not ret:
    primeiroPonto   = obterDados("Informe a distância do primeiro ponto: ")
    segundoPonto    = obterDados("Informe a distância do segundo ponto: ")
    ret = validacaoPontos(primeiroPonto, segundoPonto)

tempoGasto = obterDados("Informe o tempo gasto no percurso: ")

velocidade = conversor(resultado(primeiroPonto, segundoPonto, tempoGasto))
clear()

print("A velocidade de foi de " + str(round(velocidade, 2)) + "Km/h." + validaMulta(velocidade))
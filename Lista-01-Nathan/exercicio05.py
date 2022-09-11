from os import system, name

def raizeX1(a, b, D):
    return (-b + D**(1/2)) / (2*a)

def raizeX2(a, b, D):
    return (-b - D**(1/2)) / (2*a)

def clear():

    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

while True:
    clear()
    print('Calculando as raízes de uma equação de 2º grau\n')
    a = float(input('Entre com o valor de a: '))
    b = float(input('Entre com o valor de b: '))
    c = float(input('Entre com o valor de c: '))
    D = (b**2 - 4*a*c)
    x1 = raizeX1(a, b, D)
    x2 = raizeX2(a, b, D)

    print("Delta: {0}".format(D))

    if(D < 0):
        print("Nenhuma raiz real")
    elif D == 0:
        print("Uma única raiz real")
        print("\nValor de x1: {0}".format(x1))
    else:
        print("Duas raizes real")
        print("\nValor de x1: {0}".format(x1))
        print("Valor de x2: {0}".format(x2))

    continua = input('Deseja sair? Digite S de sair ou Enter para novo cálculo:')
    
    clear()

    if(continua == 'S' or continua == 's'):
        break
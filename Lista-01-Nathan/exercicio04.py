def validacao(entrada):
    return True if entrada > 0 else False

def motivoErro(valor, descicao):
    if valor < 0: 
        print("O valor informado da " + str(descicao) + " é Negativo!")
    else:
        print("O valor informado da " + str(descicao) + " é Zero!")

ret = False    
while not ret:

    base    = int(input("Infome a base: "))

    ret = validacao(base)

    if not ret:
        print("Valor inválido!")
        motivoErro(base, "BASE")


ret = False
while not ret:

    altura  = int(input("Infome a altura: "))

    ret = validacao(altura)

    if not ret:
        print("Valor inválido!")
        motivoErro(altura, "ALTURA")


area = base * altura/2

print("O valor da área do triângulo é " + str(area))
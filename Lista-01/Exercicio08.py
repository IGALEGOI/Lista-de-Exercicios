larguraSalao = int(input('Largura do salão (m)? '))
comprimentoSalao = float(input('Comprimento do salão (m)? '))

larguraPiso = float(input('Largura do piso (mm)? '))
comprimentoPiso = float(input('Comprimento do piso (mm)? '))

pecasLargura = int((1000 * larguraSalao) // larguraPiso) + 1
pecasComprimento = int((1000 * comprimentoSalao) // comprimentoPiso) + 1

totalPecas = pecasLargura * pecasComprimento

print('No peças para largura =', pecasLargura)
print('\nNo peças para comprimento =', pecasComprimento)
print('\nTotal de Pecas =', totalPecas)
custoEtanol = float(input('Preço do litro do etanol? '))
custoGasolina = float(input('Preço do litro da gasolina? '))

custoTanqueEtanol = custoEtanol * 50
custoTanqueGasolina = custoGasolina * 50

relacao_EtanolGas = custoEtanol / custoGasolina

relacao_GasEtanol = custoGasolina / custoEtanol

print('Tanque 50l Etanol é ', custoTanqueEtanol)
print('\nTanque 50l Gasolina é ', custoTanqueGasolina)
print('\nRelação Etanol/Gasolina é ', relacao_EtanolGas)
print('\n1 l Gasolina = ', relacao_GasEtanol, 'l Etanol')
valor = float(input('Qual sálario do funcionário: R$'))
calculo = valor + (valor * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}' .format(valor, calculo))

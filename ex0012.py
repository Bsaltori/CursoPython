valor = float(input('Qual o preço do produto: R$'))
desconto = valor - (valor * 5 / 100)
print('O valor do produto R${:.2f} com 5% de desconto fica R${:.2f}' .format(valor, desconto))
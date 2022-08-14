km = float(input('Qual a quantidade de KM percorridos pelo seu carro: '))
dias = int(input('Qual a quantidade de dias que o seu carro foi alugado: '))
resul = (km * 0.15) + (dias * 60)
print('O valor a pagar é de: R${:.2f}'.format(resul))

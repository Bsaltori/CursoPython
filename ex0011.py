n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))
area = n1 * n2
tinta = area / 2
print('Sua parede tem a dimensão de {}x{}, e sua área é de {}m²' .format(n1, n2, area))
print('Para pintar essa área, você precisará de {} litros de tinta' .format(tinta))
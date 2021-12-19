larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = larg * alt
litros = area / 2
print('Sua parece tem a dimensão de {} x {} e sua área é de {:.2f}.'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(litros))

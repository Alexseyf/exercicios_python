dias = int(input('Por quantos dias o carro esteve alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
vdia = 60*dias
vkm = 0.15*km
vtotal = vdia + vkm
print('O valor a pagar é de R${:.2f}.'.format(vtotal))

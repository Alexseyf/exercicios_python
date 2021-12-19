preco = float(input('Informe o Valor do produto: R$ '))
desc = (preco*5/100)
novopreco = preco - desc
print('O produto que custava R${:.2f}, na promoção custará R${:.2f} com desconto de 5%.'.format(preco, novopreco))
print('O desconto total foi de R$ R${:.2f}.'.format(desc))

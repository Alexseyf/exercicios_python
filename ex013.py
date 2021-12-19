salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario*15/100
novosalario = salario + aumento
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passará a receber R${:.2f}.'.format(salario, novosalario))
print(('Isso representa um aumento de R${:.2f} em seu salário.'.format(aumento)))

salario = float(input('qual seu salario atual?'))
novo = salario + (salario * 15 / 100)
print('seu salario atual é R${:.2f} com o aumento de 15% seu salario agora é R${:.2f}'.format(salario , novo))

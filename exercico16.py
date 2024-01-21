diasp = float(input(' quantos dias ficou com  veiculo: '))
km = float(input('qual a quilometragem percorida: '))
valordia = diasp * 60 
valorkm = km * 0.15
total = valordia + valorkm
print('o total a pagar é R${}'.format(total ))

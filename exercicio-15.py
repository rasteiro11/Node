dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados'))
total = (dias * 60) + (km * 0.25)
print('o valor total a pagar e de {}'.format(total))
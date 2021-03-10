v = float(input('qual o valor do produto? R$ '))
m = int(input("""
	[1] à vista.
	[2] à vista no cartão.
	[3]parcelamento no cartão em até 2X.
	[4]parcelamento no cartão em até 3X ou mais.

qual sua opcão? """))
if m == 1:
    print('o valor final é R${:.2f}.'.format(v - (v / 100 * 10)))
elif m == 2:
    print('o valor final é R${:.2f}.'.format(v - (v / 100 * 5)))
elif m == 3:
    print('o valor final é R${:.2f}.'.format(v + (v / 100 * 10)))
elif m == 4:
    p = int(input('parcelar quantas vezes? '))
    if p <= 2:
        print('parcelamento errado')
    else:
        print('o valor final é R${:.2f}.'.format(v + (v / 100 * 20)))
else:
    print('opção invalida!')



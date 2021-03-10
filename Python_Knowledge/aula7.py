nome = str(input('qual e o teu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem')
else:
    print('seu nome e tao normal!')
print('bom dia, {}!'.format(nome))

#######################################
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua media foi boa PARABENS!')
else:
    print('sua media foi ruim! ESTUDE MAIS!')
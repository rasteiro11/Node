nome = str(input('qual e seu nome? '))
if nome == 'Gustavo':
    print('que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome e bem popular no brasil. ')
elif nome in 'Ana Claudia Jessica Juliana':
    print('belo nome feminino')
else:
    print('seu nome e bem normal. ')
print('tenha um bom dia {}!'.format(nome))
nome = input(str('digite seu nome completo: ')).strip()#elimina os espacos antes e depois
print('analisando seu nome... ')
print('seu nome em maiusculas em {}'.format(nome.upper()))
print('seu nome em minusculas em {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome e {} e tem {} letras'.format(separa[0], len(separa[0])))
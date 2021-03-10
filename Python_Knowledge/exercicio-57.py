
sexo = str(input('informe seu sexo: [M,F]'))
while sexo not in 'MF':
    sexo = str(input('dados invalidos. favor informar o seu sexo'))
print('sexo {} registrado com sucesso'.format(sexo))

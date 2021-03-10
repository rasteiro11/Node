print('\033[30mOla, mundo') #30 == brannco
print('\033[31mOla, mundo') #31 == vermelho
print('\033[32mOla, mundo') #32 == verde
print('\033[33mOla, mundo') #33 == amarelo
print('\033[34mOla, mundo') #34 == azul
print('\033[35mOla, mundo') #35 == roxo
print('\033[36mOla, mundo') #36 == azul claro
print('\033[37mOla, mundo') #37 ==  cinza

nome = 'Rafael'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'# antes do ';' indica o style que pode ser 0 1 4==sublinhado e 7==highlited
        }
print('ola muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome,cores['limpa']))

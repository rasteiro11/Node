n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
menu = 0
while menu != 5:
    print('escolha uma opção no menu')
    menu = int(input(('''
    1: para soma
    2: para multiplicar
    3: para ver qual e o maior
    4: para escolher novos numeros
    5: para sair do programa
    digite aqui: ''')))
    if menu == 1:
        soma = n1 + n2
        print('a soma entre {} e {} e de {}'.format(n1, n2, soma))
    if menu == 2:
        multi = n1 * n2
        print('o numero {} multiplicado por {} e {}'.format(n1, n2, multi))
    if menu == 3:
        if n1 > n2:
            print('o numero {} e o maior'.format(n1))
        if n2 > n1:
            print('o numero {} e maior'.format(n2))
    if menu == 4:
        n1 = int(input('digite um novo numero'))
        n2 = int(input('digite mais um novo numero'))
    elif menu == 5:
        print('programa filalizado')
    else:
        print('opção invalida')
print('fim do programa')
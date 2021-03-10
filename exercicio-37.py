num = int(input('digite um numero inteiro: '))
print('''escolhha uma das bases de conversao :
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('sua opcao: '))
if opcao == 1:
    print('{} convertido em BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('opcao invalida')



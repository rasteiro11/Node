a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem e menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem e o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))
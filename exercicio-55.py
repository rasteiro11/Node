maior = 0
marior = 0
for p in range(1, 6):
    peso = float(input('peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}KG'.format(maior))
print('o menor peso lido foi de {}KG'.format(menor))
somaidade = 0
mediaidade = 0
maioridaedehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('-----------{} PESSOA------------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridaedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridaedehomem:
        maioridaedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('a media de idade do grupo e {}'.format(mediaidade))
print('o homem mais velho do grupo tem {} e se chama {}'.format(maioridaedehomem, nomevelho))
print('ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
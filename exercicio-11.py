largura = float(input('Largura da parede: '))
altura = float(input('Altura de sua parede'))
area = largura * altura
tinta = area / 2
print('sua parede tem a dimensao de {} x {} e sua area e de {} metros quadrados, para pintar essa parede voce precisara de {} litros de tinta'.format(largura, altura, area, tinta))

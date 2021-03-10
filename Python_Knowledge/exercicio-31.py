viagem = int(input('Digite a distância da sua viagem em km : '))
if viagem <= 200:
  custo = (viagem * 0.50)
  print('O custo dessa viagem é de {} reais !'.format(custo))
else:
  taxa = (viagem * 0.45)
  print('A taxa para essa viagem mais longa passa a ser de {} reais! '.format(taxa))



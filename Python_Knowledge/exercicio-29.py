velocidade = float(input('qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/h')
    multa = (velocidade - 80) * 7
    print('voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com seguranca!')
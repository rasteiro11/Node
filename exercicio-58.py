from random import randint
computador = randint(0, 10)
print('sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('sera que voce consegue adivinhar')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('diga seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez.')
print('acertou com {} tentativas. Parabens'.format(palpites))
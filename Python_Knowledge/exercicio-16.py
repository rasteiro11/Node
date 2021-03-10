#import math
from math import trunc #assim o math.trunc(num) deve ser retirado
num = float(input('Digite um valor: '))
print('o valor digitdo foi {} e a sua porcao inteira e {}'.format(num, trunc(num)))
########################################
num = float(input('Digite um valor: '))
print('o valor digitdo foi {} e a sua porcao inteira e {}'.format(num, int(num)))
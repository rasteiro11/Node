import math
import emoji
import random
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} e igual a {}'.format(num, raiz))
#######################################
num = random.random()
print(num)
#######################################
nummint = random.randint(1, 10)
print(nummint)
#######################################
print(emoji.emojize("ola mundo :sunglasses:", use_aliases=True))
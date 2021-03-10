import math
angulo = float(input('digite o angulo que voce quiser'))
seno = math.sin(math.radians(angulo))
print('o angulo {} tem o seno de {:.2f}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('o angulo {} tem o cosseno de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('o angulo {} tem a tangente de {:.2f}'.format(angulo, tan))
n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
s = n1 + n2
print('a soma vale {}'.format(s))

##############################################
# 1 -> () parenteses
# 2 -> ** exponenciacao
# 3 -> * multiplicacao,/ divisao,// divisao inteira,% resto da divisao
# 4 -> + soma,- subtracao
##############################################
print(5 + 3 * 2)
print(5**2)
print(5**3)
print(19//2)
print(19/2)
print(18%2)
print(122%3)
print(4**3)
print(pow(4,3))
print(81**(1/2))
print(25**(1/2))
print(127**(1/3))
print('oi' + 'ola')
print('oi' * 5)
print('=' * 20)
#############################################
nome = input('qual e o seu nome')# nome = str(input('qual e o seu nome'))
print('prazer {}'.format(nome))
print('prazer {:20}'.format(nome)) #coloca a string nome com espaco na memoria de 20 espacos
print('prazer {:>20}'.format(nome)) #alinha a direita a string nome
print('prazer {:<20}'.format(nome)) #alinha a esquerda a string nome
print('prazer {:^20}'.format(nome)) #centraliza a string nome
print('prazer {:=^20}'.format(nome)) #colocara a string nome em 20 espacos e  ira preenche-los com '='
#############################################
n1 = int(input('Um valor'))
n2 = int(input('outro valor'))
print('a soma vale {}'.format(n1 + n2))

#############################################

n1 = int(input('Um valor'))
n2 = int(input('outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma e {}, \n o produto e {},e a \n divisao e {:.3f}'.format(s, m, d), end= ' ')#end para nao quebrar a linha
print('divisao intrira {}, e poteniacao{}'.format(di, e))                                #\n p quebrar
                                                                                         #{:.3f}indica 3 casas apos o ponto flutuante ou float

#############################################
#Desafio 5

num1 = int(input('Digite um número para saber seu antecessor e predecessor:'))
ant = num1-1
pred = num1+1
print('O antecessor deste número é {} e seu predecessor é {}'.format(ant,pred))

# DESAFIO 6

num = int(input('Por favor, digite mais um número para saber seu dobro, triplo e raíz quadrada:'))
dobro = num*2
triplo = num*3
rq = num**(1/2)

print('O número escolhido é {}, cujo dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(num, dobro, triplo, rq))

# DESAFIO 7

hist = int(input('Qual foi sua nota em História?'))
mat = int(input('Qual foi sua nota em Matemática?'))
media = (hist + mat)/2

print('A média das suas notas foi de {}'.format(media))

# DESAFIO 8

metros = int(input('Digite um valor em METROS para ser convertido em cm e mm:'))
cm = metros*100
mm = metros*1000
print('A conversão resultante é: {} metros é igual a {}cm ou {}mm'.format(metros,cm,mm))

# DESAFIO 9

print('Vamos lá, agora precisamos criar uma tabuada')
tabuada = int(input('Escolha um número para fazermos sua tabuada de 0 à 10:'))
tab0 = tabuada*0
tab1 = tabuada*1
tab2 = tabuada*2
tab3 = tabuada*3
tab4 = tabuada*4
tab5 = tabuada*5
tab6 = tabuada*6
tab7 = tabuada*7
tab8 = tabuada*8
tab9 = tabuada*9
tab10 = tabuada*10
print('A tabuada resultante é:\n {}x0={} \n {}x1={} \n {}x2={} \n {}x3={} \n {}x4={} \n {}x5={} \n {}x6={} \n {}x7={} \n {}x8={} \n {}x9={} \n {}x10={}'.format(tabuada,tab0,tabuada,tab1,tabuada,tab2,tabuada,tab3,tabuada,tab4,tabuada,tab5,tabuada,tab6,tabuada,tab7,tabuada,tab8,tabuada,tab9,tabuada,tab10))

# DESAFIO 10

print('Agora temos um conversor de dólar, o dólar está custando R$3,27')
dolar = float(input('digite um valor em DÓLAR para converter para REAL:'))
conv = dolar*3.27
print('O valor de {:.2f} dólares equivale a {:.2f} reais, ESTAMOS QUEBRADOS!!'.format(dolar,conv))

# DESAFIO 11

print('Vamos calcular a área de uma parede para então pintá-la (em metros quadrados) e saber quanta tinta será necessária.')
alt = float(input('Qual a altura da parede?'))
larg = float(input('Qual a largura da parede?'))
area = alt*larg
print('A área da parede é de {:.3f} metros quadrados'.format(area))
tinta = area/2
print('Você então precisará de {:.1f} litros de tinta'.format(tinta))

# DESAFIO 12

preco = float(input('Qual o preço do produto?'))
desconto = preco-(preco*0.05)
print('O valor com desconto de 5% do produto é de R${:.2f}'.format(desconto))

# DESAFIO 13

salario = float(input('Parabéns, você ganhará um aumento de salário! Digite aqui seu salário atual:'))
aumento = float(input('Digite agora quanto % será aumentado do salário:'))
salaument = salario+(salario*(aumento/100))
print('Parabéns, seu salário foi aumentado para {:.2f}'.format(salaument))
casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestacao sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('emprestimo pode ser CONCEDIDO')
else:
    print('emprestimo negado')

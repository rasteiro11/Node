salario = float(input('qual o salario do funcionario'))
novo = salario + (salario * 15 / 100)
print('um funcionario que ganha R${:.2f}, com 15% de aumento , passa a receber R${:.2f}'.format(salario, novo))
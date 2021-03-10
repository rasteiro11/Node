peso = float(input("qual e seu peso? (Kg) "))
altura = float(input("qual e a sua altura? (m) "))
imc = peso / (altura ** 2)
print("o IMC dessa pessoa e de {:.1f}".format(imc))
if imc < 18.5:
    print("voce esta ABAIXO DO PESO normal")
elif 18.5 <= imc < 25:
    print("voce esta na faixa de peso normal")
elif 25 <= imc < 30:
    print("voce esta em sobrepeso")
elif 30 <= imc < 40:
    print("voce esta em obesidade")
elif imc >= 40:
    print("voce esta em obesidade morbida cuidado")
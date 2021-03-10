nota1 = float(input("sua primeira nota"))
nota2 = float(input("sua segunda nota"))
print("tirando {} e {}, sua media sera {}".format(nota1, nota2, (nota1+nota2)/2))
if (nota1+nota2)/2 <= 5:
    print("seu aluno esta de recuperacao")
elif (nota1+nota2)/2 >= 5:
    print("seu aluno foi aprovado")


r1 = float(input("Primneiro lado"))
r2 = float(input("Segundo lado"))
r3 = float(input("Terceiro lado"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triangulo!", end="")
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISOSCELES")
else:
    print("Os segmentos acima nao podem formar um tringulo")

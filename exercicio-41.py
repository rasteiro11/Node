from datetime import date
anoa = date.today().year
datan = int(input("ano de nascimento:"))
calssificacao = anoa - datan
if calssificacao <= 9:
    print("este e um candidato MIRIM")
elif calssificacao <= 14:
    print("este e um candidato INFANTIL")
elif calssificacao <= 19:
    print("este e um candidato JUNIOR")
elif calssificacao <= 25:
    print("este e um candidato SENIOR")
else:
    print("este candidato e MASTER")

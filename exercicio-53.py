frase = str(input('digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('o inverso de {} e {}'.format(junto, inverso))
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um polindromo!')
else:
    print('a frase digitada nao e um palindromo')
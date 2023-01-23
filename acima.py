# dado 3 numeros, indica quantos deles são maiores do que a media aritmetica

numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

media = (numero1 + numero2 + numero3) / 3

acima = 0

if numero1 > media:
  acima = acima + 1

if numero2 > media:
  acima = acima + 1

if numero3 > media:
  acima = acima + 1

print(acima)

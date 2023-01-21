# imprime o numero da casa das unidades

numero = int(input())

if numero > 0:
  print(numero % 10)

if numero < 0:
  numero = numero * -1
  print((numero % 10) * -1)

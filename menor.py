# menor numero

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

menor = numero1

if numero2 < menor:
  menor = numero2

if numero3 < menor:
  menor = numero3

print(menor)

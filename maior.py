entrada = input().split()

numero1 = int(entrada[0])
numero2 = int(entrada[1])
numero3 = int(entrada[2])

def MaiorAB(numero1, numero2):
  maior = (numero1 + numero2 + abs(numero1 - numero2)) / 2
  return maior

def MaiorABC(numero1, numero2, numero3):
  maiorDeDois = MaiorAB(numero1, numero2)
  maiorDeTodos = MaiorAB(numero3, maiorDeDois)
  return '%.0i eh o maior' % maiorDeTodos

print(MaiorABC(numero1, numero2, numero3))

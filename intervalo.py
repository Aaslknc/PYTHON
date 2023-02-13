def intervalo(numero):
  if numero < 0 or numero > 100:
    return 'Fora de intervalo'
  elif numero >= 0 and numero <= 25:
    return 'Intervalo [0,25]'
  elif numero <= 50:
    return 'Intervalo (25,50]'
  elif numero <= 75:
    return 'Intervalo (50,75]'
  elif numero <= 100:
    return 'Intervalo (75,100]'

numero = float(input())
resultado = intervalo(numero)
print(resultado)

# determina se o triangulo e isosceles, escaleno ou equilatero

ladoA = float(input())
ladoB = float(input())
ladoC = float(input())

if ladoA == ladoB and ladoB == ladoC:
  print('equilatero')

elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
  print('escaleno')

else:
  print('isosceles')

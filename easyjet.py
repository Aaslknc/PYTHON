largura = float(input())
comprimento = float(input())
altura = float(input())

if largura <= 45 and comprimento <= 56 and altura <= 25:
  print('PERMITIDA')

if largura > 45 or comprimento > 56 or altura > 25:
  print('PROIBIDA')

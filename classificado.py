# precisa de 100 pontos no mínimo para ser classificado

pontos1 = int(input())
pontos2 = int(input())
pontos3 = int(input())
pontos4 = int(input())
pontos5 = int(input())
pontos6 = int(input())

classificado = (pontos1 + pontos2 + pontos3 + pontos4 + pontos5 + pontos6) >= 100

if classificado:
  print('Classificado')

if not classificado:
  print('Eliminado')

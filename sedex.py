# averigua se uma bola hipotética cabe em uma caixa hipotética

diametro = int(input())
entrada = input().split()

altura = float(entrada[0])
largura = float(entrada[1])
profundidade = float(entrada[2])

if altura >= diametro and largura >= diametro and profundidade >= diametro:
  print('S')

if altura < diametro or largura < diametro or profundidade < diametro:
  print('N')

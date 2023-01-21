# calcula varios tipos de media de acordo com o input

tipo = input()
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

mediaArit = (numero1 + numero2 + numero3) / 3
mediaHarm = 3 / (1/numero1 + 1/numero2 + 1/numero3)
mediaGeom = (numero1 * numero2 * numero3)**(1/3)

if tipo == 'G':
  print('%.3f' % mediaGeom)

if tipo == 'A':
  print('%.3f' % mediaArit)

if tipo == 'H':
  print('%.3f' % mediaHarm)

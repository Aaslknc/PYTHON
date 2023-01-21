# indica se o ano inserido como entrada é bissexto ou não

ano = int(input())

condicao = (ano % 100 == 0) and (ano % 400 != 0)
condicao2 = (ano % 100 != 0) and (ano % 400 != 0)

if ano % 4 == 0 and not condicao:
  print('BISSEXTO')

if condicao:
  print('NAOBISSEXTO')

if condicao2 and ano % 4 != 0:
  print('NAOBISSEXTO')

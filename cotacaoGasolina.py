galaoEUA = float(input())
litroBRA = float(input())
cotaDolar = float(input())
# 1 galão equivale a 3,8 litros
realEUA = (galaoEUA * cotaDolar) / 3.8

print('Gasolina EUA: R$ %.2f' % realEUA)
print('Gasolina Brasil: R$ %.2f' % litroBRA)

if litroBRA == realEUA:
  print('Igual')
elif litroBRA < realEUA:
  print('Mais barata no Brasil')
else:
  print('Mais barata nos EUA')

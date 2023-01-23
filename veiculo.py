# isso aqui deu um trabalho danado

dias = int(input())
kmTotal = float(input())

cota = 100 * dias 

if dias > 1 and kmTotal > cota:
  valorTotal = ((kmTotal - cota) * 12) + (dias * 90)

if dias > 1 and kmTotal <= cota:
  valorTotal = dias * 90

if dias <= 1 and kmTotal > cota:
  valorTotal = 90 + ((kmTotal - cota) * 12)

if dias <= 1 and kmTotal <= cota:
  valorTotal = 90

print('%.2f' % valorTotal)

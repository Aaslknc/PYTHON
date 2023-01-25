# calcula o consumo de energia pra vc

consumo = int(input())

conta = 0

if consumo <= 99:
  valorPorKwh = 1.35

elif consumo >= 100 and consumo <= 299:
  valorPorKwh = 1.55

elif consumo >= 300 and consumo <= 574:
  valorPorKwh = 1.75

elif consumo >= 575:
  valorPorKwh = 2.15

if consumo > 300:
  conta = consumo * valorPorKwh
  conta = conta + (conta * 0.1)

else:
  conta = consumo * valorPorKwh
  if conta < 35:
    conta = 35

print('%.2f' % conta)
print(valorPorKwh)
  



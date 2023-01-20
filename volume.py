# Volume e area de um cilindro

pi = 3.14

altura = float(input())
raio = float(input())

volume = pi * (raio**2) * altura
area = (2 * pi * raio * altura) + 2 * pi * (raio**2)

print('%.2f' % volume)
print('%.2f' % area)

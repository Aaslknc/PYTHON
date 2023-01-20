# calcula varias areas

pi = 3.14159
entrada = input().split()

valorA = float(entrada[0])
valorB = float(entrada[1])
valorC = float(entrada[2])

areaTriangulo = (valorA * valorC) / 2
areaCirculo = pi * (valorC**2)
areaTrapezio = ((valorA + valorB) * valorC) / 2
areaQuadrado = valorB**2
areaRetangulo = valorA * valorB

print('TRIANGULO: %.3f' % areaTriangulo)
print('CIRCULO: %.3f' % areaCirculo)
print('TRAPEZIO: %.3f' % areaTrapezio)
print('QUADRADO: %.3f' % areaQuadrado)
print('RETANGULO: %.3f' % areaRetangulo)

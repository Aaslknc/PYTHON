#O comprimento de cada lado de um tri�ngulo � menor que a soma dos outros dois lados
def tipo_triangulo(lado1,lado2,lado3):
    
    soma12 = lado1 + lado2
    soma23 = lado2 + lado3
    soma13 = lado1 + lado3
    if not(soma12 > lado3 and soma23 > lado1 and soma13 > lado2):
        return 'INVALIDO'
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        return 'ESCALENO'
    elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        return 'EQUILATERO'
    else:
        return 'ISOSCELES'
        
        
while True:
    entrada = input().split()
    if entrada[0] == 'FIM':
        break
    else:
        ladoA = int(entrada[0])
        ladoB = int(entrada[1])
        ladoC = int(entrada[2])
        print(tipo_triangulo(ladoA,ladoB,ladoC))
        continue

numero1 = int(input())
numero2 = int(input())
acumulador = numero2

while True:
    
    if acumulador == 0:
        print('sem multiplos menores que %i' % numero2)
        break
    elif acumulador % numero1 == 0:
        print(acumulador)
        break
    elif acumulador % numero1 > 0:
        acumulador -= 1

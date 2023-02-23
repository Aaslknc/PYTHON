# imprime os numeros impares entre dois numeros

numero1 = int(input())
numero2 = int(input())
acumulador = 0

if numero1 % 2 != 0:
    while True:
        print(numero1 + acumulador)
        acumulador += 2
        if numero1 + acumulador > numero2:
            break
        
else: 
    numero1 += 1
    while True:
        print(numero1 + acumulador)
        acumulador += 2
        if numero1 + acumulador > numero2:
            break

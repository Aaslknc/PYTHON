numero1 = int(input())
numero2 = int(input())
acumulador = 0


while True:
    if numero1 <= 0 and numero2 <= 0:
        acumulador = 0
    elif numero1 <= 0 and numero2 > 0: # crescente
        while numero2 > 0:
            acumulador += numero2
            numero2 -= 1
            
    elif numero1 > 0 and numero2 <= 0:
        while numero1 > 0:
            acumulador += numero1
            numero1 -= 1
    elif numero1 > 0 and numero2 > 0:
        if numero2 == numero1:
            acumulador = 0
        elif numero2 > numero1:
            while numero2 != numero1 - 1:
                acumulador += numero2
                numero2 -= 1
        elif numero1 > numero2:
            while numero1 != numero2 - 1:
                acumulador += numero1
                numero1 -= 1
            
    
    
    print(acumulador)
    break

# imprime se sao iguais ou diferentes

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if numero1 == numero2 and numero2 == numero3:
    print(1)
    
elif numero1 != numero2 and numero2 != numero3 and numero1 != numero3:
    print(2)
    
else:
    print(3)

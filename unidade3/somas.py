'''A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. 
   Proponha um algoritmo recursivo que calcule a multiplicação de dois inteiros. Você só poderá usar o operador soma.
'''


def multi(num1,num2):
    
    if num2 == 0:
        return 0
    elif num2 > 0: # multiplicar por numero positivo
        if num2 == 1:
            return num1
        else:
            return num1 + multi(num1, num2 - 1)
        
    elif num2 < 0: # multiplicar por numero negativo
        if num2 == -1:
            return -num1
        else:
            return -num1 + multi(num1,num2 + 1)
    
numero1 = int(input())
numero2 = int(input())

print(multi(numero1,numero2))

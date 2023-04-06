# Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.

def pares(num):
    if num % 2 == 0:
        return num
    else:
        return pares(num - 1)
    
numero = int(input())
for i in range(numero, -1, -1):
    if i % 2 == 0:
        print(pares((i)))
        

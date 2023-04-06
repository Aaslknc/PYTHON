'''Escreva um programa que receba como entrada 5 números inteiros positivos, 
e exiba a soma dos fatoriais daqueles que são múltiplos de 3.
'''

def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)
    
def somar_valores(lista):
    soma = 0
    for elem in lista:
        soma += elem

    return soma
    
numeros = []
j = 0
for i in range(5):
    numero = int(input())
    if numero % 3 == 0:
        numeros.append(numero)
        numeros[j] = fatorial(numeros[j])
        j += 1

print(somar_valores(numeros))

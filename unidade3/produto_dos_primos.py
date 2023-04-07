'''
Dados 04 números inteiros, calcule o produto entre eles caso os 04 números digitados sejam números primos.
Se algum deles não for primo, imprima: SEM PRODUTO
'''

def ePrimo(numero):
    if numero == 1:
        return False
    e_primo = True

    for i in range(2, 10001):
        if i != numero:
            if numero % i == 0:
                e_primo = False
                break
    
    return e_primo

entrada = input().split()
n1 = int(entrada[0])
n2 = int(entrada[1])
n3 = int(entrada[2])
n4 = int(entrada[3])

if ePrimo(n1) and ePrimo(n2) and ePrimo(n3) and ePrimo(n4):
    print(n1 * n2 * n3 * n4)
else:
    print("SEM PRODUTO")

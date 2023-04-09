'''
Escreva uma função recursiva chamada ContaDigitosPares que receba como entrada um número e retorne a quantidade de dígitos pares que o compõem.
Ex: 234 tem 3 dígitos, mas apenas 2 são pares
'''

def ContaDigitosPares(numero):
    if numero == "":
        return 0
    else:
        if int(numero[0]) % 2 == 0:
            return 1 + ContaDigitosPares(numero[1:])
        else:
            return ContaDigitosPares(numero[1:])
            
numero = input()
print(ContaDigitosPares(numero))

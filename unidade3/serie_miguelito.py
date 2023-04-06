'''
Miguelito gosta muito de séries numéricas e resolveu criar uma com seu nome. 
O primeiro valor da série de Miguelito é 3, e cada novo número é gerado somando-se ora 4 ora 1 ao valor anterior, 
de acordo com o exemplo abaixo:

3  7  8  12  13  17  18  22  23  27 ...

Escreva uma função recursiva chamada SerieMiguelito que receba como entrada o índice do elemento na sequência 
e retorne seu valor.'''

def SerieMiguelito(num):
    if num == 1:
        return 3
    else:
        if num % 2 == 0: # se o indice for par, ele soma 4
            return 4 + SerieMiguelito(num - 1)
        else: # senao, ele soma 1 com o indice anterior (que será par)
            return 1 + SerieMiguelito(num - 1)
        
numero = int(input())
print(SerieMiguelito(numero))

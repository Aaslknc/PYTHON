# cria a sec logica

numero = int(input())

def primeiraLinha(num):
    return "%i %i %i" % (num, num**2, num**3)
    
def segundaLinha(num):
    return "%i %i %i" % (num, (num**2) + 1, (num**3) + 1)

for i in range(1,numero + 1):
    print(primeiraLinha(i))
    print(segundaLinha(i))
    

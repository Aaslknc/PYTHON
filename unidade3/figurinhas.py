def contar_joao(lista):
    n_figurinhas = 0
    for serie in lista:
        if serie % 2 == 0:
            n_figurinhas += 1

    return n_figurinhas

def contar_maria(lista):
    n_figurinhas = 0
    for serie in lista:
        if serie % 2 == 1:
            n_figurinhas += 1

    return n_figurinhas

def contar_ganhador(lista):
    soma_pares = 0
    soma_impares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma_pares += lista[i]
        else:
            soma_impares += lista[i]

    if soma_pares > soma_impares:
        return soma_pares
    else:
        return soma_impares

n_figurinhas = int(input())
figurinhas = []
series = {}

for i in range(n_figurinhas):
    figurinha = int(input())
    figurinhas.append(figurinha)
    series[figurinha] = series.get(figurinha,0) + 1

print(contar_joao(figurinhas))
print(contar_maria(figurinhas))
print(contar_ganhador(list(series.keys())))

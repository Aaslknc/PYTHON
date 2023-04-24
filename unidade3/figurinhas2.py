# fiz a função contar figurinhas retornar uma lista, para evitar ter duas funçoes fazendo praticamente a mesma coisa
# nao sei se essa questao era pra ser tao grande assim, mas...
def contar_figurinhas(lista):
    figurinhas_pares = 0
    figurinhas_impares = 0
    for serie in lista:
        if serie % 2 == 0:
            figurinhas_pares += 1
        else:
            figurinhas_impares += 1

    return [figurinhas_pares,figurinhas_impares]

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

print(contar_figurinhas(figurinhas)[0])
print(contar_figurinhas(figurinhas)[1])
print(contar_ganhador(list(series.keys())))

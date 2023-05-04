def multiplicar_matriz(fator, matriz):
    nova_matriz = []
    for linha in matriz:
        nova_linha = []
        for item in linha:
            nova_linha.append(item * fator)

        nova_matriz.append(nova_linha)

    return nova_matriz


def imprimir_linhas(lista):
    linha = ""
    for i in range(len(lista)):
        linha += str(lista[i]) + " "

    return linha[0: len(linha) - 1]

ordem = int(input())
matriz = []

for i in range(ordem):
    entrada = input().split()
    matriz.append([int(k) for k in entrada])

fatores = input().split(",")

for i in range(len(fatores)):
    matriz_multiplicada = multiplicar_matriz(int(fatores[i]), matriz) # converti fatores[i] para inteiro
    for linha in matriz_multiplicada:
        print(imprimir_linhas(linha))

    matriz = matriz_multiplicada
    print()

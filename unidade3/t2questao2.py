# MATRIZES DE 2 ELEVADO A J+I
# questao 2 da turma 2

def gerar_matriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            elemento = 2**(j+i)
            linha.append(elemento)

        matriz.append(linha)

    return matriz

def imprimir_lista(lista):
    stri = ""
    for i in range(len(lista)):
        stri += str(lista[i]) + " "

    return stri[0:len(stri)-1]


ordem = int(input())
while ordem != 0:
    m= gerar_matriz(ordem)

    for linha in m:
        print(imprimir_lista(linha))

    print()
    ordem = int(input())

# primeiro estudo com matrizes

tamanho = int(input())

matriz = []
for i in range(tamanho):
    entrada = input().split()
    linha = [int(k) for k in entrada]
    matriz.append(linha)
    
for elem in matriz:
    print(elem)
    

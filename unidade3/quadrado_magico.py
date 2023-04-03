# quadrado magicoooooo

tamanho = int(input())

def gerar_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        entrada = input().split()
        linha = [int(k) for k in entrada]
        matriz.append(linha)
        
    return matriz
    
def somar_horizontal(matriz):
    somas = []
    for linha in matriz:
        soma = 0
        for elem in linha:
            soma += elem
            
        somas.append(soma)
        
    return somas
    
def somar_vertical(matriz):
    somas = []
    for i in range(len(matriz)):
        soma = 0
        for elem in matriz:
            soma += elem[i]
            
        somas.append(soma)
        
    return somas
    
def somar_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        j = i
        soma += matriz[i][j]
        
    return soma
    
def somar_diagonal_inversa(matriz):
    soma = 0
    for i in range(len(matriz)):
        j = (len(matriz)-1) - i
        soma += matriz[i][j]
        
    return soma
    
matriz = gerar_matriz(tamanho)

def e_magico(matriz):
    if somar_diagonal(matriz) == somar_diagonal_inversa(matriz):
        if somar_vertical(matriz) == somar_horizontal(matriz):
            return True
    
    return False

if e_magico(matriz):
    print(somar_diagonal(matriz))
else:
    print(-1)

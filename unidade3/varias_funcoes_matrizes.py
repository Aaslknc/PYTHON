tamanho = int(input())

def gerar_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        entrada = input().split()
        linha = [int(k) for k in entrada]
        matriz.append(linha)
        
    return matriz
    


def imprimir_matriz(matriz):
    for elem in matriz:
        print(elem)
        
    return ""
        

    
def somar_horizontal(matriz):
    for linha in matriz:
        soma = 0
        for elem in linha:
            soma += elem
            
        print("Soma horizontal: %i" % soma)
        
    return ""
    
def somar_vertical(matriz):
    for i in range(len(matriz)):
        soma = 0
        for elem in matriz:
            soma += elem[i]
            
        print("Soma vertical: %i" % soma)
        
    return ""


def somar_tudo(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma += matriz[i][j]
            
    return "Soma de todos os elementos: %i" % soma
    

def somar_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        j = i
        soma += matriz[i][j]
        
    return "Soma da diagonal: %i" % soma
    

def somar_diagonal_inversa(matriz):
    soma = 0
    for i in range(len(matriz)):
        j = (len(matriz)-1) - i
        soma += matriz[i][j]
        
    return "Soma da diagonal inversa: %i" % soma
    

matriz = gerar_matriz(tamanho)
imprimir_matriz(matriz)
print(somar_horizontal(matriz))
print(somar_vertical(matriz))
print(somar_diagonal(matriz))
print(somar_diagonal_inversa(matriz))
print(somar_tudo(matriz))

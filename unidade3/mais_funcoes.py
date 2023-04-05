#somar e subtrair

m_a = [[3,4],[-1,5],[8,0]]
m_b = [[2,3],[-7,7],[0,-4]]

def somar_matrizes(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        soma = 0
        linha = []
        for j in range(len(matriz1[i])):
            
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
            
        resultado.append(linha)
        
    return resultado
    
print(somar_matrizes(m_a,m_b))

def subtrair_matrizes(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        soma = 0
        linha = []
        for j in range(len(matriz1[i])):
            soma = matriz1[i][j] - matriz2[i][j]
            linha.append(soma)
            
        resultado.append(linha)
        
    return resultado
    
print(subtrair_matrizes(m_a,m_b))

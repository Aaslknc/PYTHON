def gerar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(2**(j+i))
            
        matriz.append(linha)
        
    return matriz

def trans_em_string(lista):
    string = ""
    for elem in lista:
        string += str(elem) + " "
        
    return string[0:len(string)-1]
    
n = int(input())

while n != 0:
    matriz = gerar_matriz(n)
    for linha in matriz:
        print(trans_em_string(linha))
        
    print()
    n = int(input())
    

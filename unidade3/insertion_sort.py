lista = [1,2,3,5,6,75,7,85,23,1,3,214,56]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        
        lista[j+1] = chave
        
    return lista
    
print(insertion_sort(lista))
        

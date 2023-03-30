lista = [9,9,9,1,3,4,5,6,78,8,8,5,23,432,676,5,6,876976,987,56,456,34,5353,1,321,31,4214]

def selection_sort(lista):
    n = len(lista)
    
    for j in range(n-1):
        min_index = j #pegar indice
        for i in range(j,n):
            if lista[i] < lista[min_index]:
                min_index = i
                
        if lista[j] > lista[min_index]: #inserir menor valor
            temp = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = temp
            
    return lista
            
print(selection_sort(lista))

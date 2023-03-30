import random

lista2 = random.sample(range(0,100), 6)
lista = [1,1,2,2,1,2,3,3,3,1,3,2]

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(j, n):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i] # troca a posicao
            
    return lista
    
print(bubble_sort(lista2))

#alternativa

def bubble_sort2(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1], lista[i]
    
    return lista
                


lista = [3,2,1]
print(bubble_sort2(lista))

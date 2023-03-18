# intercalar arrays

tamanho_lista = int(input())
lista1 = []
lista2 = []
lista3 = []

for i in range(tamanho_lista):
    entrada = int(input())
    lista1.append(entrada)

for i in range(tamanho_lista):
    entrada = int(input())
    lista2.append(entrada)

for i in range(tamanho_lista):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    
for numero in lista3:
    print(numero)

tamanho = int(input())
elementos = input().split()
lista = [int(x) for x in elementos]

def listaParaString(lista):
    nova_string = ""
    for i in lista:
        nova_string += "%i " % i
        
    return nova_string[0:len(nova_string)-1]

def inverter(lista):
    lista_invertida = []
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
        
    return lista_invertida

def deslocar(lista):
    lista_deslocada = []
    for i in range(1,len(lista)):
        lista_deslocada.append(lista[i])
    
    lista_deslocada.append(lista[0])
    return lista_deslocada
    
print(listaParaString(inverter(lista)))
print(listaParaString(deslocar(lista)))
print(listaParaString(sorted(lista, reverse = True)))

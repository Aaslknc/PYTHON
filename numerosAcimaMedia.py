numero = int(input())
notas = []

for i in range(numero):
    nota = float(input())
    notas.append(nota)
    
media = sum(notas) / len(notas)
print("%.2f" % media)

def acimaDeDez(lista, media):
    nova_lista = []
    for i in range(len(lista)):
        if lista[i] > media:
            nova_lista.append(lista[i])
    
    return nova_lista
    
def abaixoDeDez(lista, media):
    nova_lista = []
    for i in range(len(lista)):
        if lista[i] < media:
            nova_lista.append(lista[i])
    
    return nova_lista
 
print(len(acimaDeDez(notas, 1.1 * media))) 
print(len(abaixoDeDez(notas, 0.9 * media)))

entrada = input().split()

def contarOcorrencia(lista):
    cont = 0
    ultimo = lista[len(lista) - 1]
    for numero in lista:
        if int(numero) == int(ultimo):
            cont += 1
    
    return "O numero %s apareceu %i vezes" % (ultimo, cont)
    
print(contarOcorrencia(entrada))

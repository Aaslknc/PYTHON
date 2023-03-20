# retorna os indices dos numeros iguais ao ultimo numero

lista = []
def pegarNumeros(lista):
    for i in range(101):
        entrada = int(input())
        lista.append(entrada)
    return lista

lista_inteira = pegarNumeros(lista)
ultimo = lista_inteira[len(lista_inteira) - 1]

for n in range(len(lista_inteira)):
    if lista_inteira[n] == ultimo and n != len(lista_inteira) -1:
        print(n)

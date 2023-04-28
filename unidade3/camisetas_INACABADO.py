n_casos = int(input())

while n_casos != 0:
    lista = []
    for i in range(n_casos):
        nome = input()
        cor, tamanho = input().split()
        lista.append(((cor, tamanho, nome)))

    lista.sort()
    for cor, tamanho, nome in lista:
        print(cor, tamanho, nome)

    print()
    n_casos = int(input())

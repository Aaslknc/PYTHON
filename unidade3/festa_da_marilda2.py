def ordenar_convidados(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        for j in range(tamanho-1-i):
            if lista[j] > lista[j+1]:
                lista[j+1], lista[j] = lista[j], lista[j+1]

    return lista

convidados = []

convidado = input()
while convidado != "FIM":
    convidados.append(convidado)
    convidado = input()

num_convidados = int(input())
convidados_ordenados = ordenar_convidados(convidados)
for convidado in convidados_ordenados:
    print(convidado)

while num_convidados != 0:

    print('-' * 50)
    for i in range(num_convidados):
        convidado = input()
        convidados.append(convidado)

    convidados_ordenados = ordenar_convidados(convidados)
    for convidado in convidados_ordenados:
        print(convidado)
    num_convidados = int(input())


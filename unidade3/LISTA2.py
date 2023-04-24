# eu fiz basicamente o mesmo em lista1, porem substitui o .sort() pela minha propia funcao ordenar_lista, que é um insertion sort básico

def ordenar_lista(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i-1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    return lista


def decidirVencedor(lista,numero_vencedor):
    ordenar_lista(lista)
    return lista[numero_vencedor - 1]
    # pois k >= 1

entrada = input().split()
n_alunos = int(entrada[0])
vencedor = int(entrada[1])

alunos = []
for i in range(n_alunos):
    aluno = input()
    alunos.append(aluno)

print(decidirVencedor(alunos, vencedor))

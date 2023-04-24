def decidirVencedor(lista,numero_vencedor):
    lista.sort()
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

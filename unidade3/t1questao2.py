# questão 2 da prova da turma1 de kalil

def corrigir(respostas):

    notas = []
    for resposta in respostas:
        nota = 0
        for i in range(len(gabarito)):
            if resposta[i] == gabarito[i]:
                nota += 1

        notas.append(nota)

    return notas

def media(respostas):
    return sum(corrigir(respostas)) / len(corrigir(respostas))


alunos = {}
entrada = input().split()

while entrada[0] != '*':
    nome = entrada[0]
    resposta = entrada[1]
    alunos[nome] = resposta
    entrada = input().split()


gabarito = input()
respostas = list(alunos.values())
print("Maior:", max(corrigir(respostas)))
print("Menor:", min(corrigir(respostas)))
print("Media: %.2f" % (media(respostas)))


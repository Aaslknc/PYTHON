gabarito = input()
entrada = input().split()

alunos = {}
notas2 = []
notas3 = {}

while entrada[0] != "9999":
    alunos[entrada[0]] = entrada[1]
    entrada = input().split()
    
def notas(gabarito, escolhas):
    acertadas = 0
    for i in range(len(gabarito)):
        if escolhas[i] == gabarito[i]:
            acertadas += 1
            
    return acertadas
    
def mais_freq(dados):
    mais_apareceu = dados[0]
    for i in range(len(dados)):
        if dados.count(dados[i]) > dados.count(mais_apareceu):
            mais_apareceu = dados[i]
            
    return mais_apareceu

q_passaram = 0
for aluno in alunos:
    print(aluno, "%.1f" % notas(gabarito,alunos[aluno]))
    notas2.append(notas(gabarito,alunos[aluno]))
    if notas(gabarito,alunos[aluno]) >= 6:
        q_passaram += 1
        

porcent_aprovacao = (q_passaram * 100) / len(alunos)
print("%.1f%%" % porcent_aprovacao)
print("%.1f" % mais_freq(notas2))
    

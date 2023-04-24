def obterInscritos(lista, dic):
    lista.sort()
    inscritos = []
    for nome in lista:
        if dic[nome] == "YES":
            inscritos.append(nome)

    for nome in lista:
        if nome not in inscritos:
            inscritos.append(nome)

    return inscritos

def obterVencedor(lista, dic):
    votaram_yes = []
    for nome in lista:
        if dic[nome] == "YES":
            votaram_yes.append(nome)
    
    vencedor = votaram_yes[0]
    for nome in votaram_yes:
        if len(nome) > len(vencedor):
            vencedor = nome
            
    return vencedor


entrada = input().split()
participantes = {}

while entrada[0] != "FIM":
    nome = entrada[0]
    opcao = entrada[1]
    participantes[nome] = opcao
    entrada = input().split()

pessoas = list(participantes.keys())
for inscrito in obterInscritos(pessoas, participantes):
    print(inscrito)

print()
print("Amigo do Habay:")
print(obterVencedor(list(participantes.keys()), participantes))

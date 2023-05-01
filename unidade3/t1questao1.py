# 1ª questão da prova de kalil

entrada = input().split()
participantes = {}

def calcular_resultado(participantes, numeros):
    acertos = []

    for participante in participantes.keys():
        acertou = 0
        for numero in numeros:
            if numero in participantes[participante]:
                acertou += 1

        acertos.append(acertou)

    return acertos


while entrada[0] != "FIM":
    nome = entrada[0]
    aposta = [k for k in entrada[1:]]
    participantes[nome] = aposta
    entrada = input().split()

numeros = input().split('-')
resultado = calcular_resultado(participantes, numeros)
pessoas = list(participantes.keys())

saida = []
for i in range(len(resultado)):
    saida.append((resultado[i], pessoas[i]))

saida.sort()
for nome, valor in saida:
    print(valor, nome*'+')


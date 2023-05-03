# quantidades de vencedores em uma aposta

def venceu(aposta, resultado):
    # somente para uma aposta
    n_acertos = 0
    for numero in aposta:
        if numero in resultado:
            n_acertos += 1

    return n_acertos == len(resultado)


def obter_vencedor(apostas, resultado):
    ganharam = 0
    for aposta in apostas.values():
        if venceu(aposta, resultado):
            ganharam += 1

    return ganharam


n_apostas = int(input())
apostas = {}
apostador = 1

for i in range(n_apostas):
    aposta = input().split(',')
    apostas[apostador] = aposta
    apostador += 1

resultado_oficial = input().split()
vencedores = obter_vencedor(apostas, resultado_oficial)
print("Total de ganhadores:", vencedores)

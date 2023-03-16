tentativas = int(input())

def somar(numero_de_tentativas):
    soma = 0
    for i in range(tentativas):
        numero = int(input())
        soma += numero
    return soma

print(somar(tentativas))

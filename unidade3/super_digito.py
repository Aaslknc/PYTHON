'''
Nós vamos definir o superdígito de um inteiro x conforme as seguintes regras:

Se x possui apenas 1 dígito, então o superdígito é x.
Caso contrário, o super dígito de x é igual ao superdígito da soma dos dígitos de x.
'''

def somar(xs):
    if xs == []:
        return 0
    else:
        return xs[0] + somar(xs[1:])


def superdigito(numero):
    numeros_inteiros = [int(k) for k in numero]
    if len(numero) == 1:
        return int(numero)
    else:
        return superdigito(str(somar(numeros_inteiros)))
    
entrada = input().split()
numero = entrada[0]
tamanho = int(entrada[1])

novo_numero = numero * tamanho
print(superdigito(novo_numero))

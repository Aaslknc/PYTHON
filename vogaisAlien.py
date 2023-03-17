# conta cuantidades

def contar_vogais(vogais, frase):
    cont_vogais = 0
    for letra in frase:
        if letra in vogais:
            cont_vogais += 1
    
    return cont_vogais
    
numero_tentativas = int(input())

for i in range(numero_tentativas):
    vogais = input()
    frase = input()
    print(contar_vogais(vogais,frase))

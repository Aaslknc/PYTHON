# soma os multiplos de 3 ou 5 menores do ue o numero N

numero = int(input())
limite_maximo = numero - 1
soma = 0

while limite_maximo > 0:
    if limite_maximo % 3 == 0 or limite_maximo % 5 == 0:
        soma += limite_maximo
    
    limite_maximo -= 1
    
print(soma)

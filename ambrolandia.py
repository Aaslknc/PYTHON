# resolve as eleições em ambrolandia

votos83 = 0
votos93 = 0
votosTotais = 0
votosNulos = 0
votosBrancos = 0


while True:
    
    entrada = int(input())
    
    if entrada == -1:
        break
    elif entrada == 83:
        votos83 += 1
        votosTotais += 1
    elif entrada == 93:
        votos93 += 1
        votosTotais += 1
    elif entrada == 0:
        votosTotais += 1
        votosBrancos += 1
    else:
        votosNulos += 1
        

porcentagem_83 = (votos83 * 100) / votosTotais
porcentagem_93 = (votos93 * 100) / votosTotais

print(votos83)
print(votos93)
print(votosBrancos)
print(votosNulos)
if votos83 > votos93:
    print(83)
else:
    print(93)
print('%.2f' % porcentagem_83)
print('%.2f' % porcentagem_93)

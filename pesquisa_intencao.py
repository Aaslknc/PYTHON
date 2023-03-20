#imprime a intencao

quantidade = int(input())
candidato = input().split()
concorrente = input().split()

def vantagem(candidato,concorrente,n):
    
    vantagem = 0
    diferenca = 0
    for i in range(n):
        if float(candidato[i]) > float(concorrente[i]):
            diferenca = float(candidato[i]) - float(concorrente[i])
            if diferenca > vantagem:
                vantagem = diferenca
                
    return vantagem
    
resultado = vantagem(candidato,concorrente,quantidade)
print("%.2f" % resultado)

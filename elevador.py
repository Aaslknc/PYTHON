# as pessoas no elevador ultrapassa a capacidade máxima ?

entrada = input().split()
numero_entradas = int(entrada[0])
capacidade_maxima = int(entrada[1])
acumulador = 0
capacidade_atual = 0
passou = False

while numero_entradas > 0:
    
    entrada2 = input().split()
    sairam = int(entrada2[0])
    entraram = int(entrada2[1])
    capacidade_atual = entraram - sairam
    acumulador += capacidade_atual
    
    if acumulador > capacidade_maxima:
        passou = True
        break
    else:
        passou = False
    
    
    numero_entradas -= 1
    
if passou:
    print('S')
else:
    print('N')

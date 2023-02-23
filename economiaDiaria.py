# o valor de hoje e maior do ue o valor de ontem + 0.5 ?

economia_total = 0
contador = 7
valor_ontem = 0
dias_economizados = 0
valor_hoje = 0

while contador > 0:
    valor_ontem = valor_hoje
    valor_hoje = float(input())
    economia_total += valor_hoje
     
    if valor_ontem == 0:
        dias_economizados = 0
    elif valor_hoje >= valor_ontem + 0.5:
        dias_economizados += 1
    
    contador -= 1
    
print('R$ %.2f' % economia_total)
print(dias_economizados)

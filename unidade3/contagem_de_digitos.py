def calc(primeiro,ultimo):
    dic = {}
    numeros = [str(k) for k in range(primeiro,ultimo+1)]
    for i in range(10):
        dic[str(i)] = 0

    for i in range(len(numeros)):
        for chave in dic.keys():
            if chave in numeros[i]:
                dic[chave] += numeros[i].count(chave)

    return list(dic.values())

entrada = input().split()

while (entrada[0] != '0') and (entrada[1] != '0'):
    primeiro = int(entrada[0])
    ultimo = int(entrada[1])
    result = calc(primeiro, ultimo)
    
    for i in range(len(result)):
        if i == len(result) - 1: # para nao escrever um espaco em branco no final
            print(result[i])
        else:
            print(result[i],end=" ")
        
    
    entrada = input().split()

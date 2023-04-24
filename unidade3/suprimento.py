def calcular_dias(suprimentos):
    cont = 0
    while suprimentos >= 1:
        suprimentos = suprimentos/2
        cont += 1

    return cont

casos_de_teste = int(input())

for i in range(casos_de_teste):
    suprimento = float(input())
    print(calcular_dias(suprimento),"dias")

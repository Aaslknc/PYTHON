# pega a quantidade de numeros positivos menores do que 50 que sao multiplos dos dois numeros

numero1 = int(input())
numero2 = int(input())

contador = 0
acumulador = 49

while acumulador > 0:
    if (acumulador % numero1 == 0) and (acumulador % numero2 == 0):
        contador = contador + 1

    acumulador -= 1
    
print(contador)

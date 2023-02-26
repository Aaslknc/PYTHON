# bro this one kinda tricky ngl

numero = int(input())
soma_resultado = 0
numerador = 1
denominador = 3
resultado = ''

if numero == 0:
    print('%.2f' % soma_resultado)
else:

    while True:
        if numero == 1:
            resultado += '%i/%i' % (numerador,denominador)
            soma_resultado += numerador / denominador
            break
        resultado += '%i/%i + ' % (numerador,denominador)
        soma_resultado += numerador / denominador
        numerador += 1
        denominador += 3
        
        numero -= 1
    
    
    print(resultado)
    print('%.2f' % soma_resultado)

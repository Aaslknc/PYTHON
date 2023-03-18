def ePrimo(numero):
    e_primo = True
    # a ideia dessa função é testar os numeros em um intervalo relativamente longo (demonstração por exaustao)
    for i in range(2, 10001):
        if i != numero:
            if numero % i == 0:
                e_primo = False
                break # pus o break para nao ocorrer processamento desnecessário
    
    return e_primo
        
numero1 = int(input())
numero2 = int(input())

if not(ePrimo(numero1)):
    print("O numero %i nao eh primo" % numero1)
elif not(ePrimo(numero2)):
    print("O numero %i nao eh primo" % numero2)
else:
    if not(ePrimo(numero1+numero2)):
        print("A soma de %i e %i nao eh um primo" % (numero1,numero2))
    else:
        print("A soma de %i e %i eh um primo" % (numero1,numero2))

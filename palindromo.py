tentativas = int(input())

# inverter
def inverte(string, acumulador = "", i = 1):
    for letra in string:
        acumulador += string[len(string) - i]
        i += 1
    return acumulador

for tentativa in range(tentativas):
    texto = input()
    texto_em_minusculo = texto.lower()
    texto_invertido = inverte(texto_em_minusculo)
    
    texto_original_concatenado = texto_em_minusculo.replace(" ", "")
    texto_invertido_concatenado = texto_invertido.replace(" ", "")
    
    if texto_original_concatenado == texto_invertido_concatenado:
        print("SIM")
    else:
        print("NAO")
    

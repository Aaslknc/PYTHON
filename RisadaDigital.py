def removerConsoantes(string):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    
    for letra in string:
        if letra in consoantes:
            string = string.replace(letra, "")
            
    return string
    
def inverterString(string):
    nova_string = ""
    i = 1
    for letra in string:
        nova_string += string[len(string) - i]
        i += 1
    
    return nova_string
    
numero_entradas = int(input())

for i in range(numero_entradas):
    risada = input()
    if not("a" in risada or "e" in risada or "i" in risada or "o" in risada or "u" in risada) or len(risada) > 50:
        print("INVALIDA")
    else:
        risada_sem_consoante = removerConsoantes(risada)
        risada_invertida = inverterString(risada_sem_consoante)
        
        if risada_sem_consoante == risada_invertida:
            print("ENGRACADA")
        else:
            print("SEM GRACA")

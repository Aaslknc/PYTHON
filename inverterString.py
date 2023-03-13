# esse codigo inverte uma string utilizando o laço for
string = input()
acumulador = ""
i = 1

for letra in string:
    acumulador += string[len(string) - i]
    i += 1
    
print(acumulador)
    

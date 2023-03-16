# remove os caracteres da lista

string = input()
remover = input()
nova_string = ""

def removerCaractere(string, remover, nova_string = ""):
    for letra in string:
        if letra in remover:
            nova_string += ""
        else:
            nova_string += letra
    
    return nova_string
    
print(removerCaractere(string, remover))

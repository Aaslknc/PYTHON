# chave = letra, valor = vezes de aparencia
letras = {}
texto = input()
for letra in texto:
    letras[letra] = letras.get(letra,0) + 1

ord = [k for k in letras.keys()] # obter as chaves do dicionario
ord.sort(reverse=True) # por em ordem alfabetica inversa

for letra in ord:
    print(letra, letras[letra])

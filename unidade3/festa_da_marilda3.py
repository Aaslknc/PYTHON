def juntar_listas(lista1,lista2):
    for item in lista2:
        lista1.append(item)
        
    return lista1
    
def ordenar(lista):
    n = len(lista)
    trocou = True
    while trocou:
        trocou = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True
        n -= 1
        
    return lista
    
convidado = input()
convidados_marilda = []
convidados_irmao = []

while convidado != "FIM":
    convidados_marilda.append(convidado)
    convidado = input()

convidado2 = input()
while convidado2 != "FIM":
    convidados_irmao.append(convidado2)
    convidado2 = input()
    
convidados_marilda.sort()
convidados_irmao.sort()

for convidado in convidados_marilda:
    print(convidado)
    
print('-'*50)
for convidado in convidados_irmao:
    print(convidado)
    
print('-'*50)

todos_os_convidados = juntar_listas(convidados_marilda,convidados_irmao)
for convidado in ordenar(todos_os_convidados):
    print(convidado)



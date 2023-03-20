# remove os duplicatos

tamanho = int(input())
array = input().split()
array_em_inteiro = [int(x) for x in array]
array_em_inteiro.sort()

def arrayParaString(array):
    nova_string = ""
    for n in array:
        nova_string += "%i " % n
        
    return nova_string[0:len(nova_string) - 1]

def removerDuplas(array):
    for elem in array:
        if array.count(elem) > 1:
            while array.count(elem) != 1:
                array.remove(elem)
    return array
        

removido = removerDuplas(array_em_inteiro)
print(arrayParaString(removido))
        

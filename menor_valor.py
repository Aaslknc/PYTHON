# pega o menor valor e imprime sua posição

tamanho_do_array = int(input())
array = input().split()
array_em_inteiro = [int(x) for x in array]

menor_valor = min(array_em_inteiro)
posicao = array_em_inteiro.index(menor_valor)

print("Menor valor:", menor_valor)
print("Posicao:", posicao)

# chave = codigo do voo, valor = numero de assentos disponiveis

voos = {}

for i in range(37):
    entrada = input().split()
    cod = int(entrada[0])
    ass = int(entrada[1])
    voos[cod] = ass
# Cada pedido de reserva é representado por um par de inteiros indicando
# , respectivamente, o número do documento de identidade do cliente e o número do voo que o cliente deseja viajar.
entrada = input().split()
while entrada[0] != "9999":
    id = entrada[0]
    n_voo = int(entrada[1])
    if n_voo not in voos.keys() or voos[n_voo] <= 0:
        print("INDISPONIVEL")
    else:
        print(id)
        voos[n_voo] = voos.get(n_voo,0) -1
    entrada = input().split()
#Caso exista disponibilidade no voo, imprima o número do documento de identidade do cliente. 
# Caso não exista disponibilidade ou não exista o voo desejado, imprima a string: INDISPONIVEL

#Lembre-se que uma vez que o cliente faz a reserva em um voo, a disponibilidade deve ser reduzida.

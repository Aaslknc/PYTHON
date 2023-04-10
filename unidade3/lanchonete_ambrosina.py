# cria um cardapio e calcula a conta total

cardapio = { }

n_produtos = int(input())
for i in range(n_produtos):
    codigo = input()
    nome = input()
    preco = float(input())
    
    cardapio[codigo] = preco
    
pedido = input()
total_a_pagar = 0
quantidade = 0

while pedido != "0":
    quantidade = int(input())
    if pedido in cardapio and quantidade > 0:
        total_a_pagar += quantidade * cardapio[pedido]
        pedido = input()
        
    else:
        pedido = input()

print("%.2f" % total_a_pagar)

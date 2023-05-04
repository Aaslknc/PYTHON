def produto_mais_vendido(dicionario):
    maior_qtde = 0
    indice = 0
    valores = list(dicionario.values()) # transformei em lista
    for i in range(len(valores)):
        if valores[i] > maior_qtde:
            maior_qtde = valores[i]
            indice = i

    item_mais_vendido = list(dicionario.keys())[indice] # transformei em lista

    return "O mais vendido foi %s com %i unidades" % (item_mais_vendido, maior_qtde)

def armazenar_produtos(dados):
    produtos = {}
    for dado in dados:
        for produto in dado:
            nome, qtde = produto.split(":") # dei um split nas string e nomeei os valores
            nome = nome.lower()
            produtos[nome] = produtos.get(nome, 0) + int(qtde) # somei a posicao produtos[nome] com a variavel qtde

    return produtos


entrada = input().split(",")
dados = [] # criei uma variavel que armazena tuplas de dados

while entrada[0] != "FIM":
    dados.append(tuple(entrada))
    entrada = input().split(",")


dicionario_de_produtos = armazenar_produtos(dados)
nomes_produtos = list(dicionario_de_produtos.keys()) # criei uma lista com os nomes dos produtos
nomes_produtos.sort()

for nome in nomes_produtos:
    print(dicionario_de_produtos[nome], nome)

print(produto_mais_vendido(dicionario_de_produtos))

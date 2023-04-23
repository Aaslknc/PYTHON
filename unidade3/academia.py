senhas = {}
nomes = []

nome = input()
while nome != "SAIR":
    nomes.append(nome)
    senha = input()
    situacao = input()
    
    senhas[senha] = situacao
    
    nome = input()
    
codigo = input()
while codigo != "-1":
    
    if codigo in list(senhas.keys()):
        nome = nomes[list(senhas.keys()).index(codigo)]
        if senhas[codigo] == "P":
            print(nome + ", " + "seja bem-vindo(a)!")
        elif senhas[codigo] != "P":
            print("Não está esquecendo de algo, "+ nome + "?" + " Procure a recepção!")
    else:
        print("Seja bem-vindo(a)! Procure a recepção!")
        
    codigo = input()

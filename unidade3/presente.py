amigos = {}

n_pessoas = int(input())
for i in range(n_pessoas):
    entrada = input().split()
    nome_amigo = entrada[0]
    presentes = [k for k in entrada[1:]]
    amigos[nome_amigo] = presentes

entrada = input().split()

while entrada[0] != "FIM":
    amigo = entrada[0]
    presente = entrada[1]
    if presente in amigos[amigo]:
        print("Uhul! Seu amigo secreto vai adorar")
    else:
        print("Tente Novamente!")
    entrada = input().split()

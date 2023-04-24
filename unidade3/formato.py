def AvaliarEmail(email):
    caracteres = [k for k in email]
    if caracteres.count('.') != 2:
        return "errado"
    elif caracteres.count('@') > 1:
        return "errado"
    elif caracteres[len(caracteres)-1] == ".":
        return "errado"
    elif caracteres[0] == "@": # provavelmente existe uma maneira mais elegante de se resolver este problema
        return "errado"        # no entando, esta é a minha solução no momento
    else:
        for i in range(len(caracteres)):
            if caracteres[i] == ".":
                if caracteres[i-1] == "@" or caracteres[i+1] == "@" or caracteres[i+1] == ".":
                    return "errado"

    return "certo"



email = input()
while email != "sair":
    print(AvaliarEmail(email))
    email = input()

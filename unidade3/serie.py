# essa uestao é a ue mais tem funcoes
def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)


def eh_primo(num): # meu xodó
    for i in range(2,num+1):
        if i != num and num % i == 0:
            return False

    return True


def proximo_primo(num): # meu xodó 2
    prox = num + 1
    while not eh_primo(prox):
        prox += 1

    return prox


def calcular_serie(n_termos):
    result = 0
    for i in range(1, n_termos+1):
        if eh_primo(i):
            result += fatorial(i) / i
        else:
            result += fatorial(i) / proximo_primo(i)

    return result

n_termos = int(input())

for i in range(1,n_termos+1):
    if eh_primo(i) and i != n_termos:
        print(str(i) + '!/' + str(i) + " +", end=" ")
        
    elif eh_primo(i) and i == n_termos:
        print(str(i) + '!/' + str(i), end="") # pra nao por um espaco vazio no final
        
    else:
        if i == n_termos:
            print(str(i) + '!/' + str(proximo_primo(i)), end="") # o mesmo ocorre aui
        else:
            print(str(i) + '!/' + str(proximo_primo(i)) + " +", end=" ")


print()
print("%.2f" % calcular_serie(n_termos))

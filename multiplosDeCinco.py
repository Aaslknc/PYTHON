entrada = input().split()

inicio = int(entrada[0])
final = int(entrada[1])

result = ""
for i in range(inicio, final+1):
    if i % 5 == 0:
        result += ("%i" + "|") % i
        

print(result[0:len(result)-1])

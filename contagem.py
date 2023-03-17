numero = int(input())

string = ""
for i in range(1,numero+1):
    
    string = ("%i" + "-") % (i)
    nova_string = string * i
    print(nova_string[0:len(nova_string) - 1])

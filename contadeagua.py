# calcula a conta de agua de acordo com o consumo

consumo = int(input())
conta = 0

if consumo <= 10:
    conta = 7
elif consumo <= 30:
    conta = (consumo - 10) + 7
elif consumo <= 100:
    conta = 27 + (consumo - 30) * 2
elif consumo > 100:
    conta = 167 + (consumo - 100) * 5 
    
print(conta)

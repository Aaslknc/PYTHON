# calcula o seu investimento

entrada = input().split()
investimento_atual = float(entrada[0])
taxa = float(entrada[1])
anos = int(entrada[2])

periodo = (anos * 12) / 3
acc = 0
rendimento_atual = 0

rendimento_atual = investimento_atual * taxa
montante = investimento_atual + rendimento_atual
for i in range(int(periodo)):
    
    print("Rendimento: %.2f Montante: %.2f" % (rendimento_atual,montante))
    rendimento_atual = montante * taxa
    montante = montante + rendimento_atual
    

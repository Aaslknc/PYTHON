#converte segundos em horas, minutos e segundos

segundos = int(input())

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(str(horas) + ':' + str(minutos) + ':' + str(segundos))

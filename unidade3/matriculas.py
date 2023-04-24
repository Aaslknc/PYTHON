entrada = input().split()
matriculas_progII = [int(k) for k in entrada]

entrada2 = input().split()
matriculas_progIII = [int(k) for k in entrada2]
matriculado_em_ambos = [k for k in matriculas_progII if k in matriculas_progIII]

for elem in matriculado_em_ambos:
    print(elem, end=" ")
    

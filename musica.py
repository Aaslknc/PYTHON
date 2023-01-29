media = float(input())
faltas = int(input())

def ClassificaAluno(media,faltas):
  if faltas <= 10 and media >= 9.5:
    return 'APROVADO COM LOUVOR'
  
  elif faltas <= 10 and media >= 7:
    return 'APROVADO'

  elif faltas > 10 and media >= 7:
    return 'REPROVADO POR FALTAS'

  else:
    return 'REPROVADO'


print(ClassificaAluno(media,faltas))

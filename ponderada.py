# funcoes baby

entrada = input().split()

nota1 = float(entrada[0])
nota2 = float(entrada[1])
nota3 = float(entrada[2])
nota4 = float(entrada[3])

def AnalisarSituacao(nota1,nota2, nota3, nota4):

  mediaPonderada = (nota1 + nota2 * 2 + nota3 * 3 + nota4 * 4) / 10
  if mediaPonderada >= 9:
    return 'aprovado com louvor'
  elif mediaPonderada >= 7:
    return 'aprovado'
  elif 3 <= mediaPonderada < 7:
    return 'prova final'
  elif mediaPonderada < 3:
    return 'reprovado'


print(AnalisarSituacao(nota1,nota2,nota3,nota4))

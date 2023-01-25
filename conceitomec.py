livros = int(input())
alunos = int(input())

alunosPorLivros = alunos / livros

if alunosPorLivros <= 8:
  print('A')

elif alunosPorLivros >= 9 and alunosPorLivros <= 12:
  print('B')

elif alunosPorLivros >= 13 and alunosPorLivros <= 18:
  print('C')

else:
  print('D')


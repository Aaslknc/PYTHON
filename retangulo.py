lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
lado4 = int(input())

def eRetangulo(lado1, lado2, lado3, lado4):
  if lado1 == lado2 and lado3 == lado4:
    return True
  elif lado1 == lado3 and lado2 == lado4:
    return True
  elif lado1 == lado4 and lado2 == lado3:
    return True
  else:
    return False

if eRetangulo(lado1, lado2, lado3, lado4):
  print('RETANGULO')
else:
  print('NAO EH UM RETANGULO')

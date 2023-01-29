# eita negocio grande da pega

dia = int(input())
mes = int(input())

def EstacaoAno(dia,mes):
  
  if 1 <= mes <= 2:
    return 'VERAO'
  elif mes == 3:
    if dia < 21:
      return 'VERAO'
    else:
      return 'OUTONO'
  elif 4 <= mes <= 5:
    return 'OUTONO'
  elif mes == 6:
    if dia < 21:
      return 'OUTONO'
    else:
      return 'INVERNO'
  elif 7 <= mes <= 8:
    return 'INVERNO'
  elif mes == 9:
    if dia < 21:
      return 'INVERNO'
    else:
      return 'PRIMAVERA'
  elif 10 <= mes <= 11:
    return 'PRIMAVERA'
  elif mes == 12:
    if dia < 21:
      return 'PRIMAVERA'
    else:
      return 'VERAO'
  
  

print(EstacaoAno(dia,mes))

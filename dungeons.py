def escolheProfissao(forca,inteligencia,destreza,furtividade,peso):
  if forca > 5 and destreza > 5 and peso > 5:
    return 'Knight'
  elif forca < 5:
    return 'Mage'
  elif forca > 5 and inteligencia > 5:
    return 'Paladin'
  elif forca > 10 and furtividade < 5:
    return 'Orc'
  else:
    return 'invalido'

forca = int(input())
inteligencia = int(input())
destreza = int(input())
furtividade = int(input())
peso = int(input())

resultado = escolheProfissao(forca,inteligencia,destreza,furtividade,peso)
print(resultado)

vel1 = float(input())
acel1 = float(input())
tempo1 = float(input())

vel2 = float(input())
acel2 = float(input())
tempo2 = float(input())

vel3 = float(input())
acel3 = float(input())
tempo3 = float(input())

def velkmh(vel,acel,tempo):
  velocidade = vel + acel * tempo
  return velocidade * 3.6

menor = velkmh(vel1,acel1,tempo1)

if velkmh(vel2,acel2,tempo2) < menor:
  print(velkmh(vel2,acel2,tempo2))

elif velkmh(vel3,acel3,tempo3) < menor:
  print(velkmh(vel3,acel3,tempo3))
else:
  print(menor)

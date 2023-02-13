def numeroIntermediario(num1,num2,num3):
  intermediario = num1
  if (num2 < num1 and num2 > num3) or (num2 > num1 and num2 < num3):
    intermediario = num2
  elif (num3 < num1 and num3 > num2) or (num3 > num1 and num3 < num2):
    intermediario = num3
  return intermediario

num1 = int(input())
num2 = int(input())
num3 = int(input())

resultado = numeroIntermediario(num1,num2,num3)
print(resultado)

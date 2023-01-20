entrada = input().split()

aguaConsumida = float(entrada[0])
custoPorLitro = float(entrada[1])

valorAgua = (aguaConsumida * 1000) * custoPorLitro
esgoto = valorAgua * 0.8
conta = valorAgua + esgoto

print('%.2f' % valorAgua)
print('%.2f' % esgoto)
print('%.2f' % conta)

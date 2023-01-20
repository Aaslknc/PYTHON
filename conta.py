consumo = float(input())

conta = consumo * 1.5
desconto = conta * 0.15
contaComDesconto = conta - desconto

print('Valor a ser pago: R$ %.2f reais' % conta)
print('Valor a ser pago com desconto: R$ %.2f reais' % contaComDesconto)

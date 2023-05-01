# AEEEEEEEEEEEEEEEEEEE CARALHOOOOOOOOOOOOOOOOOOOOOOO

num1 = float(input())
num2 = float(input())
acumulador = num1

opr = input()
while opr != "&":
    if opr == '+':
        acumulador += num2
        print('%.3f' % (acumulador))
    elif opr == '-':
        acumulador += -num2
        print('%.3f' % (acumulador))
    elif opr == '*':
        acumulador *= num2
        print('%.3f' % (acumulador))
    elif opr == '/':
        if num2 != 0:
            acumulador /= num2
            print('%.3f' % (acumulador))
        else:
            print('operacao nao pode ser realizada')

    num2 = float(input())
    opr = input()

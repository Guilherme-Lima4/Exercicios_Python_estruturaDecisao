import math

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    Rdelta = math.sqrt(delta)
    x1 = (-b + Rdelta) / 2 * a
    x2 = (-b - Rdelta) / 2 * a
    print ("As duas raizes diferentes obtidas foram: ", x1, x2)   
else:
    if delta == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
        print ("As raizes sao iguais: ", x1, x2)
    else:
        if delta < 0:
            print ("Nao existem raizes reais")      
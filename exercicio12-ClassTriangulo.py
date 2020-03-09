l1 = float(input("Informe o valor do primeiro lado do triangulo: "))
l2 = float(input("Informe o valor do segundo lado do triangulo: "))
l3 = float(input("Informe o valor do terceiro lado do triangulo: "))

if l1 == l2 and l2 == l1 and l1 == l3 and l2 == l3 and l3 == l1 and l3 == l2:
    print ("Este e um triangulo equilatero")
else:
    if l1 == l2 and l2 == l1 or l3 == l2 and l2 == l3 or l1 == l3 and l3 == l1:
        print ("Este e um triangulo isoceles")
    else:
        if l1 != l2 and l2 != l3 and l3 != l1:
            print ("Este e um triangulo escaleno")    
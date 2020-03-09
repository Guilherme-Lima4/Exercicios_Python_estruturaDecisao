n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))
n3 = float(input("Informe o terceiro numero: "))
n4 = float(input("Informe o quarto numero: "))

if n1 == n2 or n2 == n1 or n1 == n3 or n3 == n1 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n2 or n3 == n4:
    print "Existem numeros repetidos !"
else:
    print "Nao existem numeros repetidos !"    
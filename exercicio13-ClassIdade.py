idade = int(input("Informe sua idade: "))

if idade <= 12:
    print ("Classificado como crianca")
else:
    if idade > 12 and idade <= 17:
        print ("Classificado como adolescente")
    else:
        if idade >= 18 and idade <= 59:
            print ("Classificado como adulto")
        else:
            if idade > 59:
                print ("Classificado como idoso")        
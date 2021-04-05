num = int(input("Digite um numero"))
cont = 1

while cont <= num:
    if num %2 == 1:
        cont = cont+1
        print("primo")
        break
    else:
        print("não primo")
        break

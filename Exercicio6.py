num = int(input("Digite um numero: "))
cont = 0
divisivel = []

for i in range(num):
    if num % (i + 1) == 0:
        cont += 1
        divisivel.append(i + 1)
    else:
        cont

if cont == 2:
    print("O numero é primo, sendo divisivel por ", divisivel)
else:
    print("O numero não é primo pois é divisivel por ", divisivel)
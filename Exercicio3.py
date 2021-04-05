#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.#

print("Seja bem vindo. Informe números para soma! Lembre-se, apenas números entre 1 e 100!")
print("Para encerrar a experiência, informe 0!")

condicao = True

soma=0
numero=[]

while condicao:
    num=int(input('Informe o valor para soma: '))

    if (num != 0) and (num >=1) and (num <= 1000):
        soma += num
        numero.append(num)
    else:
        print("Você encerrou a ação.")
        break

print('Soma: ', soma)
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))

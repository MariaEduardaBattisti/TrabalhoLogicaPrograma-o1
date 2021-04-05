#Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.#
print("Seja bem vindo. Informe números para soma!")
print("Para encerrar a experiência, informe 0!")

condicao = True

soma=0
numero=[]

while condicao:
    num=int(input('Informe o valor para soma: '))

    if num != 0:
        soma += num
        numero.append(num)
    else:
        print("Você encerrou a ação.")
        break

print('Soma: ', soma)
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))
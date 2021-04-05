#Altere o programa de cálculo do fatorial,
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a
# números inteiros positivos e menores que 16.#
print("Seja bem vindo. Use 0 para parar a ação.")
print("Apenas números inteiros, maiores que 0 e menores que 16.")
condicao = True

soma = 0
numero = []
while condicao:
    num = int(input("Insira um número para fazer fatorial: ") )

    if (num != 0) and (num < 16):
        resultado=1
        count=1
        while count <= num:
            resultado *= count
            count += 1
        print(resultado)

    else:
        print("Você parou a ação.")
        break


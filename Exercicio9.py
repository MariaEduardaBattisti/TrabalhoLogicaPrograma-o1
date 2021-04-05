contador = 0
soma_idades = 0

comecar= input("Deseja informar uma idade? S para sim, N para não.")
print("Para fechar lancamentos de idade, digite N.")
while comecar == "S":
    idade =(input("Idade: "))

if idade < 0:
    print("idade inválida.")

    if idade == "N":
        soma_idades = soma_idades + int(idade)
        contador = contador + 1
        media = soma_idades / contador

    if media >= 0 and media <= 24:
        print("Jovem, média de ", media, " anos.")
    if media >= 26 and media <= 60:
        print("adulta, média de ", media, " anos.")
    if media > 60:
        print("idosa, média de ", media, " anos.")



eleitores = int(input("Insira o total de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for votos in range(eleitores):
    b = input("vote em a, b, ou c: ")
    if b == "a":
        candidato1 = candidato1 + 1
    elif b == "b":
        candidato2 = candidato2 + 1
    elif b == "c":
        candidato3 = candidato3 + 1

print("O candidato A ficou com ", candidato1, "votos. O candidato B ficou com ", candidato2, "votos. O candidato C ficou com ", candidato3,"votos. ")
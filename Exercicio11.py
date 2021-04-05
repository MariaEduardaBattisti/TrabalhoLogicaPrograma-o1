turmas = int(input("Quantas turmas na instituição? : "))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print("turma ", turma)
    alunos = int(input("Quantidade de alunos da turma : "))
    while alunos > 40:
        print("turma ", turma, " [uma turma só pode ter 40 alunos]")
        alunos = int(input("Quantidade de alunos da turma : "))
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print("A media e igual a: ", media)
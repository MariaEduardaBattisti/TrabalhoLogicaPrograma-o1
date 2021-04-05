resultado = 'sS'
soma = 0
quantidade = 0

while resultado == sS:
    notas = float(input("Digite a nota: "))
    resultado = str(input("Deseja continuar? [S / N]: "))
    soma += notas
    quantidade += 1
    media = soma / quantidade


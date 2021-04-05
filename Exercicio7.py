numero =  int(input('Digite um número:  '))
resultado = 0

for c in range(1, n1 + 1):
    if numero % c == 0:
        print(' \033[34m' , end='')
        resultado += 1
    else:
        print(' \033[31m' , end='')
    print(f'{c}', end='')

print(f'\n\33[mO número {numero} foi divisivel {result} vezes!')

if result == 2:
    print('E por isso é um número Primo!')
else:
    print('E por isso não é um número Primo!')
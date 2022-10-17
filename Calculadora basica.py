while True:
    print()
    num_1 = input('Digite um numero: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro numero: ')
    sair = input('Deseja sair? sim ou não: ')

    if sair == 'sim':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print('Resultado:', num_1 + num_2, )
    elif operador == '-':
        print('Resultado:', num_1 - num_2, )
    elif operador == '/':
        print('Resultado:', num_1 / num_2, )
    elif operador == '*':
        print('Resultado:', num_1 * num_2, )
    else:
        print('Operador invalido')
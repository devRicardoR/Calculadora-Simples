while True:
    try:
        primeiro_numero = float(input('Digite o primeiro número: '))
        segundo_numero = float(input('Digite o segundo número: '))
        operador = input('Escolha o operador desejavel (+,-, * ou /): ')
        if operador not in "+-*/":
            print('Erro! Operador inválido.')
        elif operador == '+':
            resultado = primeiro_numero + segundo_numero
            print(f"A soma entre {primeiro_numero} e {segundo_numero} "
                  f"é igual a {resultado}. ")
        elif operador == '-':
            resultado = primeiro_numero - segundo_numero
            print(f"A subtração entre {primeiro_numero} e {segundo_numero} "
                  f"é igual a {resultado}. ")
        elif operador == '*':
            resultado = primeiro_numero * segundo_numero
            print(f"A multiplicação entre {primeiro_numero} e {segundo_numero} "
                  f"é igual a {resultado}. ")
        elif operador == '/':
            if segundo_numero == 0:
                print('Erro, 0 é um número indivisivel! ')
            else:
                resultado = primeiro_numero / segundo_numero
                print(f'A divisão entre {primeiro_numero} e {segundo_numero} '
                      f'é igual a {resultado}. ')
    except ValueError:
        print('Erro! Digite um número: ')
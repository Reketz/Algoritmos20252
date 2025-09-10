numero = int(input('Digite um numero: '))
centenas = 0
if numero < 1000:
    if numero >= 100:
        centenas = numero // 100
        numero = numero - centenas * 100
        if centenas == 1:
            print(f'{centenas} centena')
        elif centenas > 1:
            print(f'{centenas} centenas')

    if numero >= 10:
        dezenas = numero // 10
        numero = numero - dezenas * 10
        if dezenas == 1:
            print(f'{dezenas} dezena')
        elif dezenas > 1:
            print(f'{dezenas} dezenas')
    
    if numero == 1:
        print(f'{numero} unidade')
    elif numero > 1:
        print(f'{numero} unidades')


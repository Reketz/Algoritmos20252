# Vamos criar um sistema de terminal simulando uma calculadora
# Ela deve perguntar qual operação deseja realizar
# Quando números deve realizar a opção
# Pedir todos os números solicitados
# Realizar operação: somar, subtrair, multiplicar e dividir

# Exemplo de menu:
# Sistema CalcPython
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 0 - Sair
# Digite uma das opções abaixo:

while True:
    opcao = input('\nSistema CalcPython\n\n1 - Somar\n2 - Subtrair\n3 - Mulplicar\n4 - Dividir\n0 - Sair\n\nDigite sua opção: ')

    if(opcao == '0'):
        break
    elif(opcao == '1'):
        numeros = int(input('Digite quantos números deseja somar: '))
        soma = 0
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            soma += valor
        print(f'O valor da soma é {soma}')
    elif(opcao == '2'):
        numeros = int(input('Digite quantos números deseja subtrair: '))
        subtrair = 0
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            if(n == 0):
                subtrair = valor
            else:
                subtrair -= valor
        print(f'O valor da subtrair é {subtrair}')
    elif(opcao == '4'):
        numeros = int(input('Digite quantos números deseja dividir: '))
        dividir = 0
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            if(n == 0):
                dividir = valor
            else:
                dividir = dividir / valor

            
        print(f'O valor da dividir é {dividir}')

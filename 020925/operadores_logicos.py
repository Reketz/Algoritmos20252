numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
operacao = input('Digite somar OU + para somar os números: ')
resultado = 0
if(operacao == 'somar' or operacao == '+'):
    resultado = numero1 + numero2
else:
    resultado = numero1 * numero2

print(f'O resultado é {resultado}')
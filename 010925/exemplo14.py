compra = float(input('Digite o valor da compra: '))
estado = input("Digite a sigla do seu estado: ")

if estado == 'PB':
    if compra > 500:
        cpf = input('Digite o seu cpf: ')
    else:
        print('Não precisa do cpf')

if estado == 'RN':
    if compra > 700:
        cpf = input('Digite o seu cpf: ')
    else:
        print('Não precisa do cpf')
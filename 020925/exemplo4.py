clienteVIP = input('Você é um cliente vip? (S / N): ')
clienteNovo = input('Você é um cliente novo? (S / N): ')
compra = float(input('Valor da compra: '))

if clienteVIP == 'S' or clienteNovo == 'S':
    compra = compra * 0.9

print(f'Total da compra: {compra}')
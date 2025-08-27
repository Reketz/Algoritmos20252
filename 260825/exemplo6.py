taxa = 5.43

print('Bem vindo ao conversor real para dólar')
valor = float(input('Digite o valor em reais: '))
dolar = valor * taxa
print(f'A conversão de R${valor} em dólar é US${dolar}')

#dolar para real

valor = float(input('Digite o valor em real: '))
dolar = valor / taxa
print(f'A conversão de R${valor} em dólar é US${dolar}')
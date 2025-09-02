compra = float(input('Digite o total da compra: '))
valorFrete = 60

if compra > 100:
    compra = compra - valorFrete
else:
    compra = compra + valorFrete

print(f'O valor total da compra+frete {compra}')
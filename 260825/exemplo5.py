# preço de um produto
# dar um desconto em X%

precoProduto = float(input('Digite o valor: '))
percentualDesconto = int(input('Digite o desconto %: '))

valorDesconto = precoProduto * percentualDesconto / 100 

print(f'Preço do produto é {precoProduto}')
print(f'Percentual do desconto é {percentualDesconto}')
print(f'Valor do desconto é: {valorDesconto}')
print(f'Preço final do produto é: {precoProduto - valorDesconto}')


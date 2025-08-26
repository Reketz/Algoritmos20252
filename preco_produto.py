# o valor de um produto é de 100 reais
# e será aplicado um desconto de 10%
# mostre ao usuário o seguinte texto:
# O produto custa R$100
# O valor do desconto é: 10%
# O valor final do produto é: X
# Onde X é o valor de 100 - 10%
preco = 100
desconto = 15

print(f'O produto custa: R$ {preco}')
print(f'O valor do desconto é: {desconto}%')

valorDesconto = preco * desconto / 100
print(f'O valor final do produto é: R$ {preco - valorDesconto}')
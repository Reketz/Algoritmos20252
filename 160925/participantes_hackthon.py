quantidade = int(input('Digite a quantidade do time: '))
ingresso = 44
valorTotal = quantidade * ingresso

if(quantidade >= 5):
    desconto = valorTotal * 0.1
    valorTotal = valorTotal - desconto

print(f'O valor total ingressos é {valorTotal}')
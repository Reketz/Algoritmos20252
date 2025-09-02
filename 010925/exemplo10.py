compra = float(input('Digite o total da compra: '))
cupomDesconto = 15

if compra >= 100:
    desconto = compra * cupomDesconto / 100
    compra = compra - desconto

print(f'O total da sua compra foi: {compra}')
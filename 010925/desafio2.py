# Crie um algoritmo que some 3 números e
# verifique se o resultado é positivo
# Se sim, imprimir: 'O resultado é positvo'
# Se não, imprimir: 'O resutlad é negativo 
# ou neutro'

# Crie um algoritmo que peça um número inteiro positivo
# Se o número for maior que 50 dobre ele
# Se não, subtraia 12% do seu valor
# Imprima o resultado final

n = int(input('Digite um numero: '))

if n > 0:
    if n > 50:
        n = n * 2
    else:
        sub = n * 12 / 100
        n = n - sub

print(f'O valor do número final é: {n}')
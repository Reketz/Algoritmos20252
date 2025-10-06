# peça números e vai somando até o usuário digitar -1
# quando o usuário digitar -1 imprima o valor total da soma
# de todos os números digitados
soma = 0

numero = int(input('Digite um numero: '))
while numero != -1:
    soma += numero
    numero = int(input('Digite um numero: '))

print('Fim do calculo')
print(f'Valor da soma {soma}')
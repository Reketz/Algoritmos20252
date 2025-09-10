salario = float(input('Digite o seu salário: '))
salario_liquido = salario
percentual = 0
valor_aumento = 0

if(salario > 0 and salario <= 280):
    percentual = 20
elif(salario > 280 and salario <= 700):
    percentual = 15
elif(salario > 700 and salario <= 1500):
    percentual = 10
elif(salario > 1500):
    percentual = 5
else:
    print('Valor inválida!')

valor_aumento = salario * percentual / 100
salario_liquido = salario + valor_aumento

print(f'Salário inicial: {salario}')
print(f'Valor do percentual {percentual}')
print(f'Valor do aumento: {valor_aumento}')
print(f'Salário final {salario_liquido}')
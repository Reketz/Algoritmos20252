valorHora = float(input('Digite o seu valor/hora: '))
quantidadeHoras = int(input('Digite o total de horas trabalhadas: '))

salarioBruto = valorHora * quantidadeHoras

print(f'+ Salário bruto : R${salarioBruto:.2f}')

impostoRenda = salarioBruto * 0.11
print(f'- IR (11%): R${impostoRenda:.2f}')
inss = salarioBruto * 0.08
print(f'- INSS (8%) : R${inss:.2f}')
sindicato = salarioBruto * 0.05
print(f'- Sindicato (5%): R${sindicato:.2f}')

salarioLiquido = salarioBruto - impostoRenda - inss - sindicato
print(f'- Salário líquido: R${salarioLiquido:.2f}')
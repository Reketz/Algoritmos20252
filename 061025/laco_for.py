# peça n notas para o usuário
# someas e calcule a média

notas = int(input('Digite n notas: '))
soma = 0
for n in range(notas):
    nota = float(input('Digite a nota: '))
    soma += nota

print(f'Valor da soma {soma}')
print(f'Média {soma / notas}')


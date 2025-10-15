# nomes = ["Debora", "Maria", "Julia", "João", "Gabriel"]

# nomes[3] = "Novo valor"

# print(nomes)

nomes = ["Debora", "Maria", "Julia", "João", "Gabriel"]

for indice in range(len(nomes)):
    print(f'Código {indice} | Nome {nomes[indice]}')

indice = int(input('Qual o nome você quer editar? (Digite o indice) '))
while indice < 0 or indice >= len(nomes):
    print('Indice é inválido')
    indice = int(input('Qual o nome você quer editar? (Digite o indice) '))

novoNome = input('Digite o novo nome: ')

nomes[indice] = novoNome

for indice in range(len(nomes)):
    print(f'Código {indice} | Nome {nomes[indice]}')




# range() é uma função que gera um lista de intervalos

# intervalos = tuple(range(10))
# print(intervalos)

# alfabeto = ["A", "B", "C", "D"]
# tam = len(alfabeto)
# indices = tuple(range(tam))

# for ind in indices:
#     print(ind, ' aponta para = ', alfabeto[ind])
# bruxos = ["Harry Potter", "Hermione", "Ronie Wesly", "Sirius Black", "Snape"]
# print("Lista antes de remover...")
# print(bruxos)

# print("Lista depois de remover...")
# bruxos.remove("Hermione")
# bruxos.remove(bruxos[1])
# print(bruxos)

# bruxos = ["Harry Potter", "Hermione", "Ronie Wesly", "Sirius Black", "Snape"]
# for b in bruxos:
#     print(f'Nome do bruxo {b}')

# bruxos.remove(input('Digite o nome do bruxo que deseja remover: '))

# for b in bruxos:
#     print(f'Nome do bruxo {b}')
bruxos = ["Harry Potter", "Hermione", "Ronie Wesly", "Sirius Black", "Snape"]

for i in range(len(bruxos)):
    print(f'Código: {i} | Nome: {bruxos[i]}')

indice = int(input('Digite o indice para remover: '))
bruxos.remove(bruxos[indice])

for i in range(len(bruxos)):
    print(f'Código: {i} | Nome: {bruxos[i]}')
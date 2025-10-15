# nomes = ["Ana", "João", "Gabriel", "Rauã", "Júlia", "Maria"]
# print("Lista antes da adição", nomes)

# novoNome = input('Digite o novo nome: ')
# nomes.append(novoNome)
# print("Lista depois da adição", nomes)

contatos = []

while True:
    print("Bem vindo a lista de contatos")
    print("1 - Cadastro novo contato")
    print("2 - Listar os contatos")
    print("3 - Alterar contato")
    print("4 - Remover contato")
    print("0 - Sair")
    opcao = input("Digite sua opção: ")
    if(opcao == "0"):
        break
    elif(opcao == "1"):
        nome = input("Digite o nome do contato: ")
        celular = input('Digite o seu celular: ')
        cidade = input('Digite a cidade: ')
        contatos.append([nome, celular, cidade])
    elif(opcao == "2"):
        print('\n\n--------------------------------')
        print('Lista de contatos\n\n')
        for cont in contatos:
            print(f'Nome {cont[0]} | Telefone {cont[1]} | Cidade {cont[2]}')
        print('--------------------------------\n\n')
    elif(opcao == "3"):
        for indice in range(len(contatos)):
            print(f'Código {indice} - Nome {contatos[indice][0]}')

        indice = int(input('Digite o indice que deseja alterar: '))
        while indice < 0 or indice >= len(contatos):
            print('Inválido')
            indice = int(input('Digite o indice que deseja alterar: '))

        nome = input("Digite o novo nome do contato: ")
        celular = input('Digite o novo seu celular: ')
        cidade = input('Digite a nova cidade: ')
        novaSublista = [nome, celular, cidade]
        contatos[indice] = novaSublista
    elif(opcao == "4"):
        for indice in range(len(contatos)):
            print(f'Código {indice} - Nome {contatos[indice][0]}')

        indice = int(input('Digite o indice que deseja remover: '))
        while indice < 0 or indice >= len(contatos):
            print('Inválido')
            indice = int(input('Digite o indice que deseja remover: '))

        contatos.remove(contatos[indice])
    else:
        print('Erro, escolha uma opção correta')



contatos = []
nome = input('Digite o nome: ')
telefone = input('Digite o nome: ')

contatos.append([nome, telefone])

for sublista in contatos:
    print(f'Nome: {sublista[0]} | Telefone: {sublista[1]}')

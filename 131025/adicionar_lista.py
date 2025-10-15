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
    else:
        print('Erro, escolha uma opção correta')



contatos = []
nome = input('Digite o nome: ')
telefone = input('Digite o nome: ')

contatos.append([nome, telefone])

for sublista in contatos:
    print(f'Nome: {sublista[0]} | Telefone: {sublista[1]}')

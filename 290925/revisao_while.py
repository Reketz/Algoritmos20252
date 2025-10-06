# contador = 10

# while contador > 0:
#     print(contador)
#     contador -= 1

# contador = int(input('Digite o número de notas que você quer?'))
# auxiliar = contador
# soma = 0

# while contador > 0:
#     nota = float(input('Digite a nota: '))
#     print(f'Nota {nota}')
#     soma = soma + nota
#     contador = contador - 1

# print(f'O valor da soma {soma}')
# print(f'O valor da média é {soma / auxiliar}')


#email = input('Digite um email válido: ')

# while "@" not in email:
#     print('Email inválido, digite novamente!')
#     email = input('Digite um email válido: ')

# senha = input('Digite um senha válido: ')

# while "*" not in senha:
#     print('senha inválido, digite novamente!')
#     senha = input('Digite um senha válido: ')

# senha = input('Digite a senha (mínimo 8 caracters): ')
# tamanho = len(senha)
# while (tamanho < 8):
#     print('Senha com caracters insuficientes...')
#     senha = input('Digite a senha (mínimo 8 caracters): ')
#     tamanho = len(senha)

senha = input('Digite a senha (mínimo 8 caracters): ')
while (len(senha) < 8 or len(senha) > 16 or ('*' not in senha)):
    print('Senha com caracters insuficientes ou não tem "*" ...')
    senha = input('Digite a senha (mínimo 8 caracters): ')

usuarios = [ ["admin", "123"], ["joaozim", "321"] ]

while True:
    nome = input('Nome: ')
    senha = input('Senha: ')
    logado = False
    usuario = []
    for u in usuarios:
        if u[0] == nome and u[1] == senha:
            logado = True
            usuario = u
            break

    if logado:
        print('Menu principal do usuário')

        break
    else:
        print('Usuário inválido')
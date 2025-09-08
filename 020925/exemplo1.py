ano = int(input('Digite seu ano de nascimento: '))
acompanhada = input('Você está acompanhada? (S/N): ')

idade = 2025 - ano

if(idade >= 18 or acompanhada == 'S'):
    print('Você entrar na festa')
else:
    print('Você não pode entrar! CAI FORA DAQUIIIIIIII!')
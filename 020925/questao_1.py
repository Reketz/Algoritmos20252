peso = float(input('Digite o valor do peso dos peixes: '))

excesso = peso - 50  
multa = excesso * 4

print(f'O peso: {peso}')
if peso > 50:
    print(f'O excesso {excesso}')
    print(f'O valor da multa é: R${multa}')
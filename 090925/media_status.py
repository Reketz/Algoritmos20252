n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

if(media == 10):
    print('Aprovado com distinção')
elif(media >= 7):
    print('Aprovado')
elif(media < 7):
    print('Reprovado')
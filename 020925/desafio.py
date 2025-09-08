n1 = int(input("Digite o n1: "))
n2 = int(input('Digite o n2: '))
maior = 0

if n1 > n2:
    print(f'O {n1} é o maior!')
    maior = n1
else:
    print(f'O {n2} é o maior!')
    maior = n2

if(maior > 0 or maior == 0):
    print(f'O {maior} é positivo ou neutro')
else:
    print(f'O {maior} é negativo')
    

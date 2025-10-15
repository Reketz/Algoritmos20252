# fruta1 = "Banana"
# fruta2 = "Abacaxi"
# fruta3 = "Maça"
# fruta4 = "Mamão"

# print(fruta2)
# fruta = input('Qual fruta deseja adicionar na cesta? ')
# cestaFrutas = [fruta, "Banana", "Abacaxi", "Maça", "Mamão"]

# print(cestaFrutas)

# numeros = [1, 2, 3, 4, 5]
# print(numeros[2])

# cestaFrutas = ["Banana", "Abacaxi", "Maça", "Mamão"]

# # print(cestaFrutas[2])
# for i in range(4):
#     print('Fruta', cestaFrutas[i])

times = ["Flamengo", "Vasco", "Corinthians", "Real Madri", "Fluminense", "Atlético"]
tamanho = len(times)

for posicao in range(tamanho):
    if posicao % 2 == 0:
        print(times[posicao])


#Imprime os valores da lista time
# for t in times:
#     print(t)
#Imprima a posição e o valor da lista time
# for posicao in range(4):
#     print(f'Posição: {posicao} time:  {times[posicao]}')
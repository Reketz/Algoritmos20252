# insert - informar o indice e o valor para adicionar na lista
# numeros = [1, 3, 4]
# numeros.insert(1, 2)

# extend - pega a lista atual e adiciona os novos valores ao final da lista
# numeros.extend([2,5,7])
# numeros.extend([9,10,15])

# print(numeros)

# frutas = ["Banana", "Maça", "Abacaxi", "Mamão", "Goiaba"]
# print(frutas)
# indice = int(input('Digite o indice que quer remover: '))
# #frutas.pop() # Remove o último valor
# frutas.pop(indice) # Remove pelo indice
# print('Lista depois da remoção do indice', frutas)

# frutas.clear() # limpeza dos registros
# print('Lista limpa', frutas)

# nums = [ 10 , 20 , 40 , 80 ]
# indice = int(input('Digite o indice que quer remover: '))
# print('Antes da remoção', nums)
# del nums[indice]
# print('Depois da remoção', nums)

#numeros = [10, 20, 30, 40, 50, 60]

#print(numeros[2:5])
#print(numeros[:5])
#print(numeros[2:])

# Exemplo para remover itens repetidos
# frutas = ["Maça", "Abacaxi", "Mamão", "Maça","Goiaba"]
# valor = input('Qual fruta você quer remover da lista: ')

# frutas = ["Maça", "Abacaxi", "Mamão", "Maça","Goiaba"]

# for i in range(len(frutas)):
#     if(i < len(frutas) and frutas[i] == "Maça"):
#         print('Indice', i)
#         frutas.pop(i)

# print(frutas)

# print(f'Lista antes de remover {frutas}')

# valor = input('Qual fruta você quer remover da lista: ')

# indice = frutas.index(valor)
# frutas.pop(indice)

# print(f'Lista depois de remover {frutas}')

#print('Número de maças: ', frutas.count("Maça"))
#print('Indice do mamão: ', frutas.index("Mamão"))

# ----------------- TUPLAS -------------------------------

# coordenadas = (10, 20)
# x, y = coordenadas
# print("x:", x)
# print("y:", y)

# a = (1, 2, 3)
# a[0] = "ALTERNADO O VALOR"

# frutas = ["Banana", "Maça", "Abacaxi", "Mamão", "Goiaba"]
# frutas[0] = "Banana da terra"

# salvar = input('Você quer salvar essa lista? ')
# if(salvar == "Sim"):
#     frutas = tuple(frutas)

# frutas[0] = "Banana nanica"

# print(frutas)

# dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
# dias_da_semana = list(dias_da_semana)

# dias_da_semana.insert(5,"Guiunda")

# print(dias_da_semana)
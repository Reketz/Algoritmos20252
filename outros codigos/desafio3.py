# Crie um algoritmo que obtenha o nome, idade e anos futuros

# Imprima: Você é o {nome} e daqui a {anos futuros}
# Você terá {novaIdade} anos  

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
anos_futuros = int(input("Digite os anos futuros: "))

nova_idade = idade + anos_futuros
print(f'Você é o {nome} e daqui a {anos_futuros} você terá {nova_idade}')


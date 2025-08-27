# 2 times (azul x vermelho) vão disputar um campeonato 
# de melhor de 3
# Crie um algoritmo que pergunte o resultado de cada partida
# Soma o placar de cada partida
# Imprima e resultado final das partidas

print('Qual o placar da primeira partida?')
timeAzul = int(input('Digite quantos pontos o time azul fez: '))
timeVerm = int(input('Digite quantos pontos o time vermelho fez: '))

print('Qual o placar da segunda partida?')
timeAzul2 = int(input('Digite quantos pontos o time azul fez: '))
timeVerm2 = int(input('Digite quantos pontos o time vermelho fez: '))

print('Qual o placar da terceira partida?')
timeAzul3 = int(input('Digite quantos pontos o time azul fez: '))
timeVerm3 = int(input('Digite quantos pontos o time vermelho fez: '))

somaTimeAzul = timeAzul + timeAzul2 + timeAzul3
somaTimeVermelho = timeVerm + timeVerm2 + timeVerm3

print('Resultado de todas as partidas...')
print(f'O time azul fez o total de {somaTimeAzul} pontos')
print(f'O time vermelho fez o total de {somaTimeVermelho} pontos')






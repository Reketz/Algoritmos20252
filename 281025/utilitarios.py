# | Método                     | Descrição                          | Exemplo                                                 |
# | --------------------------------- | ---------------------------------------------- | ------------------------------------- |
# | `int(x)`                          | Converte para inteiro.                         | `int('10')` → `10`                    |
# | `float(x)`                        | Converte para float.                           | `float('3.14')` → `3.14`              |
# | `str(x)`                          | Converte para string.                          | `str(10)` → `'10'`                    |
# | `bool(x)`                         | Converte para booleano.                        | `bool([])` → `False`                  |
# | `list(x)` / `tuple(x)` / `set(x)` | Converte iterável em lista, tupla ou conjunto. | `list('abc')` → `['a', 'b', 'c']`     |
# | --------------------------------- | ---------------------------------------------- | ------------------------------------- |
# | `str.lower()`      | Converte todos os caracteres para minúsculas.       | `'Python'.lower()` → `'python'`            |
# | `str.upper()`      | Converte todos os caracteres para maiúsculas.       | `'Python'.upper()` → `'PYTHON'`            |
# | `str.title()`      | Primeira letra de cada palavra em maiúscula.        | `'olá mundo'.title()` → `'Olá Mundo'`      |
# | `str.capitalize()` | Primeira letra em maiúscula e o resto em minúscula. | `'ola MUNDO'.capitalize()` → `'Ola mundo'` |
# | `str.swapcase()`   | Inverte maiúsculas e minúsculas.                    | `'PyThOn'.swapcase()` → `'pYtHoN'`         |
# | -------------------------- | ---------------------------------- | ------------------------------------------------------- |
# | `str.replace(velho, novo)` | Substitui partes do texto.         | `'banana'.replace('na', 'ha')` → `'bahaha'`             |
# | `str.split(sep)`           | Divide a string em uma lista.      | `'a,b,c'.split(',')` → `['a','b','c']`                  |
# | `str.join(iterável)`       | Junta elementos com o separador.   | `'-'.join(['a','b','c'])` → `'a-b-c'`                   |
# | -------------- | ----------------------------------------------- | --------------------------------- |
# | `str.strip()`  | Remove espaços (ou caracteres) do início e fim. | `'  texto  '.strip()` → `'texto'` |
# | `str.lstrip()` | Remove do início.                               | `'  texto'.lstrip()` → `'texto'`  |
# | `str.rstrip()` | Remove do fim.                                  | `'texto  '.rstrip()` → `'texto'`  |
# frutas = ["Abacate P", "Amora", "Banana", "Coco"]

# buscar = input('Digite a fruta que deseja buscar: ')

# for f in frutas:
#     if buscar in f:
#         print(f)

# pergunta = input('Deseja continuar? (S/N)').upper()

# if pergunta == 'S':
#     print('ele deseja continuar...')

# descricao = "banho e tosa"
# print(descricao.replace("banho", "chuveirada"))

# texto = 'andre,luiz,mariana,mario'
# nomes = texto.split(',')

# print(nomes[0])

# nome = input('Digite o seu nome: ').strip()

# while len(nome) < 3:
#     nome = input('Digite o seu nome: ').strip()

# print('Parabéns seu nome se enquadra', nome)
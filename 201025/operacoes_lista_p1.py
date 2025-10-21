# uso do insert
pokemons = ["Pikachu", "Charmander"]
pokemons.insert(1, "Squirtle")
print(pokemons)

# uso do extend
pokemons.extend(["Eevee", "Snorlax"])
print(pokemons)

# uso do operador "+" para juntar 2 listas
v = [ 1 , 3 , 5 ] + [ "oi" , "tchau" ]
print(v)

# uso do pop ou pop(1) <- passando o indice

pokemons.pop()
print(pokemons)

# uso do clear
pokemons.clear()
print(pokemons)

# outra forma de deletar
nums = [ 10 , 20 , 40 , 80 ]
del nums [ 2 ]
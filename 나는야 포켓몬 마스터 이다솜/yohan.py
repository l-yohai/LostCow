import sys

n, m = list(map(int, sys.stdin.readline().split()))

pokemons = list(sys.stdin.readline().strip() for _ in range(n))
questions = list(sys.stdin.readline().strip() for _ in range(m))

pokemon_to_index = {}
index_to_pokemon = {}
for i in range(len(pokemons)):
    pokemon_to_index[pokemons[i]] = str(i + 1)
    index_to_pokemon[str(i + 1)] = pokemons[i]

for i in range(m):
    if questions[i].isdigit():
        print(index_to_pokemon[questions[i]])
    else:
        print(pokemon_to_index[questions[i]])

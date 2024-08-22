from Pokedex import Pokedex
from helper.WriteAJson import writeAJson

# Inicializa a Pokedex
pokedex = Pokedex(database="pokedex", collection="pokemons")

while True:
    print("\nEscolha uma opção para o pokedex entre 1-8")
    print("1-Mostrar todos os pokemons")
    print("2-Mostrar os dados pelo nome do pokemon")
    print("3-Listar pokemons pelo tipo")
    print("4-Listar pokemons pelos tipos e que possuem evolução")
    print("5-Listar pokemons pela fraqueza")
    print("6-Listar pokemons que possuem quatro fraquezas")
    print("7-Listar pokemons que são de um certo tipo, ou fracos contra certo tipo")
    print("8-Sair da pokedex")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        pokemons = pokedex.mostrarPokemons()
        writeAJson('all_pokemons.json', pokemons)
        print("Todos os pokemons foram listados e salvos em 'all_pokemons.json'.")
    elif opcao == 2:
        nome = str(input("Digite o nome do pokemon: "))
        pokemon = list(pokedex.getPokemonByName(nome))
        writeAJson(f'{nome}.json', pokemon)
        print(f"Dados do {nome} foram salvos em '{nome}.json'.")
    elif opcao == 3:
        tipos = input("Digite os tipos de pokemon separados por vírgula: ").split(',')
        pokemons = pokedex.getPokemonsByType(tipos)
        writeAJson('pokemons_by_type.json', pokemons)
        print(f"Pokemons do(s) tipo(s) {tipos} foram listados e salvos em 'pokemons_by_type.json'.")
    elif opcao == 4:
        tipos = input("Digite os tipos de pokemon separados por vírgula: ").split(',')
        pokemons = pokedex.getPokemonsByTypeOrType(tipos)
        writeAJson('pokemons_by_type_and_evolution.json', pokemons)
        print(f"Pokemons do(s) tipo(s) {tipos} com evolução foram listados e salvos em 'pokemons_by_type_and_evolution.json'.")
    elif opcao == 5:
        fraquezas = input("Digite as fraquezas dos pokemons separadas por vírgula: ").split(',')
        pokemons = pokedex.getPokemonsByWeaknesses(fraquezas)
        writeAJson('pokemons_by_weaknesses.json', pokemons)
        print(f"Pokemons com fraqueza(s) {fraquezas} foram listados e salvos em 'pokemons_by_weaknesses.json'.")
    elif opcao == 6:
        pokemons = pokedex.getPokemonsByFourthWeaknesses()
        writeAJson('pokemons_with_four_weaknesses.json', pokemons)
        print("Pokemons com exatamente quatro fraquezas foram listados e salvos em 'pokemons_with_four_weaknesses.json'.")
    elif opcao == 7:
        tipo = input("Digite o tipo de pokemon ou fraqueza: ")
        pokemons = pokedex.getPokemonsByTypeOrByWeaknesses(tipo)
        writeAJson('pokemons_by_type_or_weakness.json', pokemons)
        print(f"Pokemons do tipo ou com fraqueza '{tipo}' foram listados e salvos em 'pokemons_by_type_or_weakness.json'.")
    elif opcao == 8:
        print("Saindo da pokedex.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1-8.")

import requests
import random

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return get_pokemon_data(api_id)['stats']

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premierPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    battle_result = 0

    for i in range(len(premierPokemon['stats'])):
        if premierPokemon['stats'][i]['base_stat'] > secondPokemon['stats'][i]['base_stat']:
            battle_result+=1
        else:
            battle_result-=1
            
    return {'winner' : first_api_id} if battle_result > 0 else {'winner' : second_api_id} if battle_result < 0 else {'winner': 'draw'}

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """

def get_random_pokemons(amount):
    """
        Return 3 random pokemon with data
    """
    randomPokeList = list()
    randomPokemonId = random.sample(range(1,1008), amount)
    for id in randomPokemonId:
        randomPoke = dict()
        randomPoke['name'] = get_pokemon_name(id)
        randomPoke['stats'] = get_pokemon_stats(id)
        randomPokeList.append(randomPoke)
    
    return randomPokeList
"""
    Handle communications with pokeapi
"""
import requests

BASE_URL = "https://pokeapi.co/api/v2"


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
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    battle_result = 0

    for index in range(len(premier_pokemon['stats'])):
        if (premier_pokemon['stats'][index]['base_stat'] >
          second_pokemon['stats'][index]['base_stat']):
            battle_result+=1
        else:
            battle_result-=1

    if battle_result > 0:
        return {'winner' : first_api_id}
    if battle_result < 0:
        return {'winner' : second_api_id}
    return {'winner': 'draw'}

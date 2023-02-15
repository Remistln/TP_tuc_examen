import datetime
import unittest
import json
from app.utils.utils import *
from unittest.mock import Mock, patch
from app.utils.pokeapi import battle_pokemon, get_random_pokemons, get_pokemon_name, get_pokemon_data, get_pokemon_stats
from app.utils.utils import age_from_birthdate


mock = Mock()


class TestPokeapi(unittest.TestCase):
    @patch('app.utils.pokeapi.get_pokemon_data')
    def test_get_pokemon_name(self, mock_get_pokemon_data):
        mock_data = {'name': 'pikachu', 'stats': [{}]}
        mock_get_pokemon_data.return_value = mock_data
        result = get_pokemon_name(25)
        self.assertEqual(result, mock_data['name'])

    @patch('app.utils.pokeapi.requests.get')
    def test_get_pokemon_data(self, mock_get):
        mock_data = {'name': 'pikachu', 'stats': [{}]}
        mock_get.return_value.json.return_value = mock_data
        result = get_pokemon_data(25)
        self.assertEqual(result, mock_data)

    @patch('app.utils.pokeapi.get_pokemon_data')
    def test_get_pokemon_stats(self, mock_get_pokemon_data):
        mock_data = {'name': 'pikachu', 'stats': [
            {"base_stat": 35, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}},
            {"base_stat": 55, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}},
            {"base_stat": 40, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}},
            {"base_stat": 90, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}]}
        mock_get_pokemon_data.return_value = mock_data
        result = get_pokemon_stats(25)
        self.assertEqual(result, mock_data['stats'])

    @patch('app.utils.pokeapi.get_pokemon_data')
    def test_battle_pokemon(self, mock_get_pokemon_data):
        mock_pokemon_1 = {'name': 'pikachu', 'stats': [
            {"base_stat": 35, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}},
            {"base_stat": 55, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}},
            {"base_stat": 40, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}},
            {"base_stat": 90, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}]}
        mock_pokemon_2 = {'name': 'charmander', 'stats': [
            {"base_stat": 39, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}},
            {"base_stat": 52, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}},
            {"base_stat": 43, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}},
            {"base_stat": 60, "effort": 0,
             "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}},
            {"base_stat": 65, "effort": 1, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}]}
        mock_data = {'winner': 4}
        mock_get_pokemon_data.side_effect = [mock_pokemon_1, mock_pokemon_2]
        mock_get_pokemon_data.return_value = mock_data
        result = battle_pokemon(25, 4)
        self.assertEqual(result, mock_data)

    @patch('app.utils.pokeapi.get_pokemon_data')
    @patch('app.utils.pokeapi.get_pokemon_name')
    @patch('app.utils.pokeapi.get_pokemon_stats')
    def test_get_random_pokemons(self, mock_get_pokemon_data, mock_get_pokemon_name, mock_get_pokemon_stats):
        mock_pokemon_1 = {'name': 'pikachu', 'stats': [
            {"base_stat": 35, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}},
            {"base_stat": 55, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}},
            {"base_stat": 40, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}},
            {"base_stat": 90, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}]}
        mock_pokemon_2 = {'name': 'charmander', 'stats': [
            {"base_stat": 39, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}},
            {"base_stat": 52, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}},
            {"base_stat": 43, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}},
            {"base_stat": 60, "effort": 0,
             "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}},
            {"base_stat": 65, "effort": 1, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}]}
        mock_pokemon_3 = {'name': 'squirtle', 'stats': [
            {"base_stat": 44, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}},
            {"base_stat": 48, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}},
            {"base_stat": 65, "effort": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}},
            {"base_stat": 50, "effort": 0,
             "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}},
            {"base_stat": 64, "effort": 0,
             "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}},
            {"base_stat": 43, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}]}
        mock_get_pokemon_data.return_value = [mock_pokemon_1, mock_pokemon_2, mock_pokemon_3]
        result = get_random_pokemons(3)
        self.assertEqual(len(result), 3)
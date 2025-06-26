import requests 
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a7e41fc701b2699d726f59b8d3247653'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '36057'


def test_status_code():
    responce = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert responce.status_code == 200

    def test_part_of_responce():
        responce_get = requests(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
        assert responce_get.json()['name'] == 'Бульбазавр'
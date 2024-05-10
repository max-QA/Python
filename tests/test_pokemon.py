import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '8293f45f31919fda2f3a5d1a4837e1ee'
HEADER = {'Contetnt-Type': 'application/json', 'trainer_token' : TOKEN}
trainer_ID = '2291'



def test_trainers():
    response_trainers = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : trainer_ID})
    assert response_trainers.status_code == 200
    assert response_trainers.json()["data"][0]["trainer_name"] == 'maxon'

@pytest.mark.parametrize('key, value', [('id', trainer_ID), ('trainer_name', 'maxon')])
def test_trainer_param(key, value):
    response_trainersss = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : trainer_ID})
    assert response_trainersss.status_code == 205
    assert response_trainersss.json()["data"][0][key] == value



'''def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : trainer_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : trainer_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', trainer_ID), ('id', '26830')])
def test_parametrize(key, value):
    response_param = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : trainer_ID})
    assert response_param.json()["data"][0][key] == value'''
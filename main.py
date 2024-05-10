import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '8293f45f31919fda2f3a5d1a4837e1ee'
HEADER = {'Contetnt-Type': 'application/json', 'trainer_token' : TOKEN}
'''body_regik = {
    "trainer_token": TOKEN,
    "email": "vaspetyr@yandex.ru",
    "password": "49FD_s544b"
}

body_confirm= {
    "trainer_token": TOKEN
}'''

body_create={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_update = {
    "pokemon_id": "26830",
    "name": "Булька",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokeboll = {
    "pokemon_id": "26830"
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_update_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update_name.text)

response_add_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeboll)
print(response_add_pokeboll.text) 



'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_regik)
print(response.text)

response_confirm = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_regik)
print(response_confirm.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''


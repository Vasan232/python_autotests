import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a7e41fc701b2699d726f59b8d3247653'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "broniboitvi1983@yandex.ru",
    "password": "Iloveqa1111"
}
body_confirmation = {
    "trainer_token":TOKEN}

body_create = {
 "name": "Бульбазавр",
 "photo_id": 12
}

'''responce = requests.post(url = f'{URL}/trainers/reg', headers = HEADER,json = body_registration)
print(responce.text)'''

'''responce_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(responce_confirmation.text)'''

responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text) 

message = responce_create.json()['message']
print(message)
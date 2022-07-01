import aiohttp
from aiogram import types
from config import ENGLENBOT_API_KEY

BASE_URL = 'http://127.0.0.1:8000/api/v1/'
PARAMS = {'format': 'json'}
TG_USER_FIELDS = {
    'tg_id': 'id',
    'first_name': 'first_name',
    'last_name': 'last_name',
    'td_username': 'username',
    'language': 'language_code',
}
HEADERS = {
    'Authorization': f'Token {ENGLENBOT_API_KEY}'
}


async def get_random_word():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL+'random_word/', params=PARAMS, headers=HEADERS) as response:
            return await response.json()


async def add_new_tg_user(user: types.User):
    async with aiohttp.ClientSession() as session:
        user_values = {key: user.values.get(val, None) for key, val in TG_USER_FIELDS.items()}
        async with session.post(BASE_URL+'add_tg_user/', params=PARAMS, json=user_values, headers=HEADERS) as response:
            return await response.json()

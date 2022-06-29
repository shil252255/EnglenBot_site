import aiohttp


async def get_random_word():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/v1/random_word/?format=json') as response:
            return await response.json()

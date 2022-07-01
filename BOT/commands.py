from aiogram import types
# from aiogram.types import message
from BOT.data_fetcher import *
from app import dp


@dp.message_handler(commands=['start'])
async def sey_hello(message: types.Message):
    """
    Приветственное сообщение.
    Пока только для проверки работоспособности.
    :param message:
    :return:
    """
    res = await add_new_tg_user(message.from_user)
    print(res)
    await message.answer('Hello!')


@dp.message_handler(commands=['random'])
async def random_word(message: types.Message):
    """
    А тут проверяю связку с API.
    :param message:
    :return:
    """
    res = await get_random_word()
    await message.reply(f"{res['word']} - {res['def_translations']}")

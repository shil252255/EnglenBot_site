from aiogram import types
# from aiogram.types import message

from app import dp


@dp.message_handler(commands=['start'])
async def sey_hello(message: types.Message):
    await message.reply('Hello!')

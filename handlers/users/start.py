from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from pymongo import MongoClient
from .funcitons import check,register

from loader import dp
import pymongo

cluster = MongoClient('mongodb://localhost:27017')
db = cluster['intelekt']
collection = db['users']


@dp.message_handler(CommandStart())
async def bot_start(ms: types.Message):
    info = ms.from_user
    tekshir = check(info.id)
    if tekshir == 'topilmadi':
        register(info.full_name, info.username, info.id)
        await ms.answer(f"Salom, {ms.from_user.full_name}!\nBazaga saqlandi")
    else:
        await ms.answer(f"Salom, {ms.from_user.full_name}!\nSiz bazada borsiz")

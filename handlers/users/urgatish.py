from aiogram.types import Message
from states.teacher import Intelekt
from aiogram.dispatcher import FSMContext
from loader import dp
from .funcitons import speach_create,speach_ok

from pymongo import MongoClient
import pymongo
import asyncio
import random as r

cluster = MongoClient('mongodb://localhost:27017')

speak = cluster['intelekt']
collection_speak = speak['speach']
dictions = []

@dp.message_handler(state=Intelekt.urgatish)
async def teachers(ms:Message,state:FSMContext):
    date = await state.get_data()
    msg = date.get('lg')
    idn = ms.from_user.id
    dictions.append((ms.text).lower())
    print(dictions)
    if len(dictions) >= 3:
        speach_create(idn,msg,dictions[0],dictions[1],dictions[-1])
        await ms.answer("<b>Yaxshi tushundim nima deyishni</b>\nEndi shunday deyman")
        dictions.clear()
        try:
            await state.finish()
        except:
            pass
    else:
        yana = await ms.answer("<b>Yana nima deyay</b> ❓")
        await ms.delete()


@dp.message_handler()
async def Spech(ms:Message,state:FSMContext):
    msg = (ms.text).lower()
    yes = speach_ok(msg).capitalize()
    print(yes)
    if yes == 'None':
        chp = await ms.answer(f"👉 \"{msg}\" nima degani\
            \n<b>Shunday xabar kelsa men nima deb javob beray</b> ❓")
        await state.update_data(lg=msg)
        await Intelekt.urgatish.set()
        await asyncio.sleep(40)
        await chp.delete()
    else:
        await ms.answer(yes)



import pymongo
from pymongo import MongoClient
import random as r

cluster = MongoClient('mongodb://localhost:27017')
user = cluster['intelekt']
collection_user = user['users']

speak = cluster['intelekt']
collection_speak = speak['speach']

trt = [15]

def register(name,link,idn):
    """Yangi qo'shilganlarni ro'yxatdan o'tkazuvchi funksiya"""
    about = {'name':name, 'link':link, 'user_id':idn}
    collection_user.insert_one(about)


def check(idn):
    """Data bazada bor yoki yo'qligini qaytaruvchi funksiya"""
    
    result = collection_user.find_one({'user_id':idn})
    if result:
        return 'bor'
    else:
        return 'topilmadi'



def speach_create(idn, query, answer1, answer2, answer3):
    """So'z o'rgatish uchun func"""
    trt.append(1)
    about = {'_id':int(max(trt)), 'user_id':idn, 'query':query, 'answer1':answer1, 'answer2':answer2, 'answer3':answer3}
    collection_speak.insert_one(about)


def speach_ok(query):
    """Bu so'zni biladimi yoki yo'q tekshirish"""
    result = collection_speak.find_one({'query':query})
    if result:
        tx = r.randint(1,3)
        return result[f'answer{tx}']
    else:
        return 'None'


import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb://localhost:27017')
db = cluster['intelekt']
collection = db['users']

post = {'_id':31,'name':'vantu','score':51}
post2 = {'_id':35,'name':'ontime','score':252}

# kim = input(">>>> ")
# collection.insert_many([post,post2]) ##Yangi table qo'shish
# result = collection.delete_one({'name':'jake'}) # ustuni ochirish
# print(result)
# for res in result:
#     print(res)
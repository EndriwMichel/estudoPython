# Utilizando MongoDb
import pymongo
import datetime
import os

mongo_pass = os.environ['mongo_access']

client = pymongo.MongoClient(mongo_pass)
db = client.cadastrodb

coll = db.posts

print(type(coll))

post1 = {'codigo': 'ID-9987725',
         'prod_name': 'Geladeira',
         'marcas': ['brastemp', 'consul', 'electrolux'],
         'data_cadastro': datetime.datetime.utcnow()}

print(type(post1))

# Função para inserir um registro
post_id = coll.insert_one(post1)

# Imprimi ID do registro 
print(post_id.inserted_id)

post2 = {'codigo': 'ID-2209876',
         'prod_name': 'Televisor',
         'marcas': ['samsung', 'panasonic', 'lg'],
         'data_cadastro': datetime.datetime.utcnow()}

post_id = coll.insert_one(post2)

print(post_id.inserted_id)

for x in coll.find():
    print(x)


print(db.name)

print(db.list_collection_names())
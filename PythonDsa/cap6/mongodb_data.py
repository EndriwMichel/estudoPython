# Retornando dados mongoDb
import pymongo
import os

mongo_pass = os.environ['mongo_access']

client = pymongo.MongoClient(mongo_pass)
db = client.cadastrodb

# db.create_collection('mycollection')

print(db.list_collection_names())

db.mycollection.insert_one({
    'titulo': 'MongoDb com Python',
    'descricao': 'MongoDb é um banco de dados NoSQL',
    'by': 'Data Science Academy',
    'url': 'http://datascienceacaemy.com.br',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'likes': 100
})

print(db.mycollection.find_one())

doc1 = {'nome': 'Donald', 'sobrenome':'Trump', 'tweeter': '@POTUS'}

db.mycollection.insert_one(doc1)

doc2 = {'site': 'http://datascienceacaemy.com.br', 'facebook':'http://facebook.com/atascienceacademy'}

db.mycollection.insert_one(doc2)

for x in db.mycollection.find():
    print(x)


col = db['mycollection']    

print(type(col))
    
print(db.mycollection.count())

redoc = col.find_one()

print(redoc)
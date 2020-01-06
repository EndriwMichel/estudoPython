# Utilizando os tweets coletados com pandas e scikit-learn
import pandas as pd
import pymongo
import os
from sklearn.feature_extraction.text import CountVectorizer

mongo_pass = os.environ['mongo_access']

client = pymongo.MongoClient(mongo_pass)
db = client.tweeterDb
col = db.tweets

# utilizando list comprehension para retornar dados do mongo db
dataset = [{'created_at': item['created_at'], 'text': item['text']} for item in col.find()]

# Criando um DataFrame com o dataset
df = pd.DataFrame(dataset)

print(df)

# Utilizando o metodo CountVectorizer para criar uma matriz de documentos
cv = CountVectorizer()
count_matrix = cv.fit_transform(df.text)

# Contando o numero de ocorrencias das principais palavras no dataset
word_count = pd.DataFrame(cv.get_feature_names(), columns=['word'])
word_count['count'] = count_matrix.sum(axis=0).tolist()[0]
word_count = word_count.sort_values('count', ascending=False).reset_index(drop=True)

print(word_count[:50])
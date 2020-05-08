# Carregar o modelo de um arquivo separado

import pickle
from ml_model import X_teste

# print(X_teste)

loadded_model = pickle.load(open('modelo_treinado_v3.sav', 'rb'))
print(X_teste[15].reshape(1, -1))
print(X_teste[18].reshape(1, -1))
print('')

resultado1 = loadded_model.predict(X_teste[15].reshape(1, -1))
resultado2 = loadded_model.predict(X_teste[18].reshape(1, -1))

print('Resultado1: ')
print(resultado1)
print('')

print('Resultado2: ')
print(resultado2)
print('')

# A pessoa do indicie 15 não tera diabetes
# A pessoa do indicie 18 tera diabetes
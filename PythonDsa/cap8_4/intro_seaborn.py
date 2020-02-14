# Trabalhando com Seaborn
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd
import random
import numpy as np

""" Obtendo dataset """
dados = sea.load_dataset('tips')

""" Criando plots """

""" Joinplot """
# sea.jointplot('total_bill', 'tip', dados, kind='reg')
# plt.show()

""" Multipleplot """
"""
Obs.: Este moelo é muito bom para rapidamente visualizar dados dividos em dois segmentos, como True ou False (Ex. Sim e Não) 
"""
# sea.lmplot('total_bill', 'tip', dados, col='smoker')
# plt.show()

""" Plot com DataFrame """
df = pd.DataFrame()

df['a'] = random.sample(range(1, 100), 25)
df['b'] = random.sample(range(1, 100), 25)

# sea.lmplot('a', 'b', data=df, fit_reg=True)
# plt.show()

""" Plot de Densidade """
# sea.kdeplot(df.b)
# plt.show()

""" Box plot """
# sea.boxplot([df.b, df.a])
# plt.show()

""" Heatmap """
# sea.heatmap([df.a, df.b], annot=True, fmt='d')
# plt.show()

""" Clustermap """
# sea.clustermap(df)
# plt.show()

""" Multiplots by variables """
g = sea.FacetGrid(dados, row='sex', col='time', margin_titles=True) 
bins = np.linspace(0, 60, 13)
g.map(plt.hist, 'total_bill', color='steelblue', bins=bins, lw=0)
plt.show()
# Imports
import pandas as pd
import numpy as np

# Carrega o arquivo
load_file = "dados_compras.json"
purchase_file = pd.read_json(load_file, orient = "records")
# pf = purchase_file.head()

# print(purchase_file.head())
# print(purchase_file['Item ID'])

# Analise geral das compras
class AnaliseComprasGeral():
    def __init__(self, file):
        self.file = file 
        print('')
        print('Analise Geral das compras !')
        pass

    def cria_df(self):
        df = pd.DataFrame(self.file, columns=['Login', 'Idade', 'Sexo', 'Item ID', 'Nome do Item', 'Valor'])
        return df

    # Função verifica itens exclusivos
    def exclusive_itens(self, data_f):
        print('')
        print('-- Número de itens exclusivos --')
        unique_itens = data_f['Item ID'].unique().tolist()
        return print(len(unique_itens))

    def avg_sales(self, data_f):
        print('')
        print('-- Preço médio de compra --')
        avg_sales_result = data_f['Valor'].mean()
        return print(avg_sales_result)

    def count_sales(self, data_f):
        print('')
        print('-- Número total de compras --')
        return print(len(data_f))

    def sum_sales(self, data_f):
        print('')
        print('-- Rendimento total --')
        sum_values = data_f['Valor'].sum()
        return print(sum_values)

# Declarando objeto
vendas = AnaliseComprasGeral(purchase_file)

# Cria dataframe que será trabalhado nos demais metodos
vendas_df = vendas.cria_df()

# Pegando itens exlusivos
vendas.exclusive_itens(vendas_df)

# Pegando média de vendas
vendas.avg_sales(vendas_df)

# Pegando o numero total de compras
vendas.count_sales(vendas_df)

# Pegando o rendimento total
vendas.sum_sales(vendas_df)


class InfosDemoGenero(AnaliseComprasGeral):
    def __init__(self, file):
        self.file = file 
        print('')
        print('Informações Demográficas Por Gênero !')
        pass

    # Porcentagem e contagem de compradores masculinos
    def male_sales(self, data_f):
        print('')
        print('-- Porcentagem e contagem de compradores masculinos --')
        male_count_arr = [x for x in data_f['Sexo'] if x == 'Masculino']
        male_count = len(male_count_arr)
        male_sales_percent = (male_count / len(data_f)) * 100
        return print('Qtd: %s - %.2f porcento'%(male_count, male_sales_percent))

    # Porcentagem e contagem de compradores famininos
    def female_sales(self, data_f):
        print('')
        print('-- Porcentagem e contagem de compradores femininos --')
        female_count_arr = [x for x in data_f['Sexo'] if x == 'Feminino']
        female_count = len(female_count_arr)
        female_sales_percent = (female_count / len(data_f)) * 100
        return print('Qtd: %s - %.2f porcento'%(female_count, female_sales_percent))

    # Porcentagem e contagem de compradores outros
    def another_sales(self, data_f):
        print('')
        print('-- Porcentagem e contagem de compradores outros --')
        another_count_arr = [x for x in data_f['Sexo'] if x != 'Feminino' and x != 'Masculino']
        another_count = len(another_count_arr)
        another_sales_percent = (another_count / len(data_f)) * 100
        return print('Qtd: %s - %.2f porcento'%(another_count, another_sales_percent))

# Instanciando objeto para analise de Informações Demográficas Por Gênero
vendas_genero = InfosDemoGenero(purchase_file)

# Reutilizano a função de recriação de dataframe 
vendas_genero_df = vendas_genero.cria_df()

# Pegando contagem e porcentagem de compradores masculinos
vendas_genero.male_sales(vendas_genero_df)

# Pegando contagem e porcentagem de compradores feminos
vendas_genero.female_sales(vendas_genero_df)

# Pegando contagem e porcentagem de compradores não definidos
vendas_genero.another_sales(vendas_genero_df)

class AnalisePorGenero(InfosDemoGenero):
    def __init__(self, file):
        self.file = file
        print('')
        print('Análise de Compras Por Gênero !')
        pass
    
    def sales_count(self, data_f):
        print('')
        print('-- Número de compras --')

        # Compradores masculinos
        male_count_arr = [x for x in data_f['Sexo'] if x == 'Masculino']
        male_count = len(male_count_arr)

        # Compradores femininos
        female_count_arr = [x for x in data_f['Sexo'] if x == 'Feminino']
        female_count = len(female_count_arr)

        # Compradores outros
        another_count_arr = [x for x in data_f['Sexo'] if x != 'Feminino' and x != 'Masculino']
        another_count = len(another_count_arr)
        return print('M: %s, F: %s, Otr.: %s'%(male_count, female_count, another_count))

    def sales_avg(self, data_f):
        print('')
        print('-- Preço médio de compra --')
        return print(data_f.groupby('Sexo')['Valor'].mean())

    def sales_sum(self, data_f):
        print('')
        print('-- Preço total de compra --')
        return print(data_f.groupby('Sexo')['Valor'].sum())

    def popular_items(self, data_f):
        five_most_popular = []
        print('')
        print('-- Itens mais populares --')
 
        np_list = np.array(data_f['Item ID'])
        item_id, counts = np.unique(np_list, return_counts=True)

        # Cria array (item id, qtd)
        count_items = list(zip(item_id, counts))

        # pega o item mais popular
        # most_popular = max(count_items, key=count_items.get)

        # return print(most_popular, count_items[most_popular])
        return print(count_items)
        
# Instancia o objeto com herança as informações demograficas por genero 
compras_genero = AnalisePorGenero(purchase_file)

# Reutilizano a função de recriação de dataframe 
compras_genero_df = compras_genero.cria_df()

# numero de compras por genero
compras_genero.sales_count(compras_genero_df)

# preço médio de copras
compras_genero.sales_avg(compras_genero_df)

# preço total de copras
compras_genero.sales_sum(compras_genero_df)

# itens mais populares
# compras_genero.popular_items(compras_genero_df)

print('')





# testes sqlite utilizando linguagem SQL
import os
import sqlite3

#os.remove('escola.db') if os.path.exists('escola.db') else None

# Conectando ao banco
con = sqlite3.connect('escola.db')

print(type(con))

cur = con.cursor()

sql_drop = 'drop table if exists cursos'

# Criando tabela
sql_create = 'create table cursos '\
    '(id integer primary key, '\
        'titulo varchar(100), '\
            'categoria varchar(140))'

cur.execute(sql_drop)
cur.execute(sql_create)

# script para efetuar insert
sql_insert = 'insert into cursos values (?, ?, ?)'

recset = [
            (1000, 'Ciencia de Dados', 'Data Science'),
            (1001, 'Big Data Fundamentos', 'Big Data'),
            (1002, 'Python Fundamentos', 'Analise de Dados'),
         ]

for x in recset:
    cur.execute(sql_insert, x)
# Pode ser usado execute many ao invez de um for
#cur.executemany(sql_insert, recset)

con.commit()

# Script para buscar os dados inseridos
sql_select = 'select * from cursos'

cur.execute(sql_select)
dados = cur.fetchall()

for x in dados:
    print('Curso id: %d, Titulo: %s, Categoria: %s'%x)

con.close()

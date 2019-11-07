# Utilizando Inserts
import sqlite3
import os
import recriaDb

def makeInsert(cursor, sql, values):
    try:
        for x in values:
            cursor.execute(sql, x)
        return True
    except:
        return print('Erro !')

# ---- Instancia classe de conexão ----
new_con = recriaDb.RecriaBanco('escola.db')

# ---- Remove banco de dados se existir ----
# new_con.removeDb() 

# ---- Cria string de conexão e de cursor para trabalhar com operações SQL ----
conn = new_con.conectionDb()
cursor = new_con.createCursor(conn)

# Recria banco de dados escola
new_con.recriaEscola(cursor)

# ---- Efetua os inserts -----

sql_insert = 'insert into cursos values (?, ?, ?)'

data = [
            (10, 'Ciencia de Dados', 'Data Science'),
            (20, 'Big Data Fundamentos', 'Big Data'),
            (30, 'Python Fundamentos', 'Analise de Dados'),
         ]

if makeInsert(cursor, sql_insert, data) is True:
    conn.commit()



# Fecha conexão com o banco
conn.close()
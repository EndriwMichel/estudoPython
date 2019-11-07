# Recria banco de dados
import os
import sqlite3

class RecriaBanco():
    def __init__(self, db_name):
        self.db_name = db_name
        
    # Metodo para remover o banco se existir    
    def removeDb(self):
        os.remove(self.db_name) if os.path.exists(self.db_name) else None
        return print('Removed db if exists')

    # Cria conexão com o banco e retorna a connection e o cursor
    def conectionDb(self):
        connect = sqlite3.connect(self.db_name)        
        print('Conexão criada !')
        return connect

    def createCursor(self, con):
        cursor = con.cursor()
        print('Cursor criado !')
        return cursor

    def recriaEscola(self, cursor):
        sql_drop = 'drop table if exists cursos'

        # Criando tabela
        sql_create = 'create table cursos '\
            '(id integer primary key, '\
                'titulo varchar(100), '\
                    'categoria varchar(140))'
        try:
            cursor.execute(sql_drop)
            cursor.execute(sql_create)
            return print('Tabela escola criada !')
        except:
            return print('erro !')


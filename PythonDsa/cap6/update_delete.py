# Update e Delete
import sqlite3

conn = sqlite3.connect('dsa.db')
cursor = conn.cursor()

# Lr os dados
def leitura_todos_dados(cursor):
    cursor.execute('SELECT * FROM produtos')
    for x in cursor.fetchall():
        print(x)

# Altera os dados com valor igual a 90.0 no banco
def altera_dados(cursor, conn):
    try:
        cursor.execute('UPDATE produtos SET valor = 900.0 WHERE valor = 90')
        conn.commit()
        return print('Dados alterados !')
    except:
        return print('Erro !')

# Remove os dados com valor igual a 480.0
def remove_dados(cursor, conn):
    try:
        cursor.execute('DELETE FROM produtos WHERE valor = 480.0')
        conn.commit()
        return print('Dados deletados !')
    except:
        return print('Erro !')

print('')
altera_dados(cursor, conn)
leitura_todos_dados(cursor)
print('')
remove_dados(cursor, conn)
leitura_todos_dados(cursor)

cursor.close()
conn.close()
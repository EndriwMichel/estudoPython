# Script python para substituir a stored procedure criada na aula
import sqlite3

class appDataBase():
    def connect(self):
        con = sqlite3.connect('PythonDsa/cap13/02-WebApp/webapp.db')
        cursor = con.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS "tbl_user" (
                            "user_id"	INTEGER,
                            "user_name"	TEXT,
                            "user_email"	TEXT,
                            "user_password"	TEXT,
                            PRIMARY KEY("user_id" AUTOINCREMENT)
                        )
                        """)
        return con             

    def insertUser(self, user_name, user_email, user_password):
        con = self.connect()

        cursor = con.cursor()
        cursor.execute("""
                        INSERT INTO tbl_user (user_name, user_email, user_password)
                        VALUES (?, ?, ?)
                        """, (user_name, user_email, user_password))
        con.commit()
        con.close()

        print('inserido !')

        return True


import sqlite3
from sqlite3 import Error



class BaseDatos():

    def crear_tabla(self):
        try:
            conn = sqlite3.connect("puntuaciones.db")
            return conn
        except Error:
            print("Error")



    def consulta(conn):
        cur = conn.cursor()
        cur.excecute('''CREATE TABLE RECORDS("nombre" text, "puntos" REAL NOT NULL, PRIMARY KEY("nombre"))''')
        conn.commit

    conn = crear_tabla





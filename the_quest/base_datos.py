import sqlite3
from sqlite3 import Error

'''

class BaseDatos():

    def crear_conexion(self):
        try:
            conn = sqlite3.connect("puntuaciones.db")
            return conn
        except sqlite3.Error as error:
            print("Se ha producido un error al crear la conexión:", error)



    def crear_tabla(conn, definicion):
        cur = conn.cursor()
        cur.excecute(definicion)
        conn.commit()

    conn = crear_tabla('records.db')

    sql = """
    CREATE TABLE records(
        nombre TEXT,
        puntos REAL NOT NULL,
        PRIMARY KEY (nombre)
    )
    """

    crear_tabla(conn, sql)

    if conn:
        conn.close()

'''



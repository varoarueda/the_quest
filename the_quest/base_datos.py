import sqlite3

class BaseDatos():
    def consultaSQL(self, consulta):
        conn = sqlite3.connect("data/puntuaciones.db")
        cur = conn.cursor()
        cur.execute(consulta)


        keys = []
        for item in cur.description:
            keys.append(item[0])

        puntuaciones = []
        for registro in cur.fetchall():
            ix_clave = 0
            d = {}
            for columna in keys:
                d[columna] = registro[ix_clave]
                ix_clave += 1
            puntuaciones.append(d)

        return puntuaciones






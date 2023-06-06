import sqlite3

conexion = sqlite3.connect('hola.db')
c = conexion.cursor()
c.execute("SELECT * FROM acciones")
print (c.fetchone())
conexion.close()
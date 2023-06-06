import sqlite3
conexion = sqlite3.connect('Ejemplo.db')

c = conexion.cursor()
c.execute(''' CREATE TABLE acciones (fecha text, operacion text, simbolo text, cantidad real, precio real)''')

c.execute("INSERT INTO acciones VALUES('24/nov/2016', 'compra', 'inv', 100, 15.43)")
c.execute("INSERT INTO acciones VALUES('09/enero/2023', 'compra', 'inv', 120, 30)")
c.execute("INSERT INTO acciones VALUES('16/mayo/2018', 'compra', 'inv', 50, 45)")
c.execute("INSERT INTO acciones VALUES('19/sep/2023', 'compra', 'inv', 30, 50)")
c.execute("INSERT INTO acciones VALUES('17/nov/2023', 'compra', 'inv', 200, 10)")
c.execute("INSERT INTO acciones VALUES('03/dic/2023', 'compra', 'inv', 180, 17)")

conexion.commit()
conexion.close()
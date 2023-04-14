import sqlite3

conexion=sqlite3.connect("BDINVENTARIO.db")      #establece la conexion

#cliente
try:
    conexion.execute("""create table cliente(
                               codC integer primary key autoincrement,
                               nombre text,
                               dni text,
                               distrito text,
                               email text

                            )""")
    print("Se creo la tabla cliente")
except sqlite3.OperationalError:
    print("La tabla cliente ya existe")

#vendedor
try:
    conexion.execute("""create table vendedor(
                               codV integer primary key autoincrement,
                               nombre text,
                               dni numeric,
                               celular numric,
                               fingreso text
                               
                            )""")
    print("Se creo la tabla vendedor")
except sqlite3.OperationalError:
    print("La tabla vendedor ya existe")



#articulo
try:
    conexion.execute("""create table articulo(
                               codA integer primary key autoincrement,
                               nombre text,
                               categoria text,
                               marca text,
                               precio real,
                               
                               
                            )""")
    print("Se creo la tabla articulo")
except sqlite3.OperationalError:
    print("La tabla articulo ya existe")
conexion.close()

'''
#cliente
conexion=sqlite3.connect("BDINVENTARIO.db")
cursor = conexion.cursor()
usuarios = [(1, "IEP PALMER", 56745376, "SJM", "PALMER@educativo.com"),
            (2, "CIBERTEC", 96786545, "Lima Centro", "cibertec@cibertec.edu.pe")
            ]
cursor.executemany("INSERT INTO cliente VALUES(?,?,?,?,?)", usuarios)
conexion.commit()
conexion.close()

#vendedor
conexion=sqlite3.connect("BDINVENTARIO.db")
cursor = conexion.cursor()
usuarios = [(1, "Ariana", 75806457, 945634567,'2020-12-25' ),
            (2, "Pablo", 64678956, 934567834,'2021-04-20')
            ]
cursor.executemany("INSERT INTO vendedor VALUES(?,?,?,?,?)", usuarios)
conexion.commit()
conexion.close()

#articulo
conexion=sqlite3.connect("BDINVENTARIO.db")
cursor = conexion.cursor()
articulo = [(1, "Nova 8i", "Celular", "Huawei", 1349.00),
            (2, "Aspiradora Vacuum", "SmartHome", "Xiaomi",1299.00),
            (3, "Mini Barebone", "Computadora", "AMD", 2403.00)
            ]
cursor.executemany("INSERT INTO articulo VALUES(?,?,?,?,?)", articulo)
conexion.commit()
conexion.close()
'''

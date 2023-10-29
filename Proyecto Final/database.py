import mysql.connector
#conn = mysql.connector.connect(**db_config)
# Función para conectar a la base de datos
def conectar_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="control_de_ventas"  # Nombre de la base de datos que creamos
        )
        return db, db.cursor()  # Retorna la conexión y el cursor
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        return None, None
    
# Función para cerrar la conexión a la base de datos
def cerrar_db(db):
    if db:
        db.close()

# Resto de funciones relacionadas con la base de datos
# Ejemplos de funciones para insertar datos

def insertar_producto(db, nombre, precio):
    cursor = db.cursor()
    try:
        query = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
        values = (nombre, precio)
        cursor.execute(query, values)
        db.commit()
        print("Producto agregado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar producto: {err}")

def insertar_cliente(db, nombre, email):
    cursor = db.cursor()
    try:
        query = "INSERT INTO clientes (nombre, email) VALUES (%s, %s)"
        values = (nombre, email)
        cursor.execute(query, values)
        db.commit()
        print("Cliente agregado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar cliente: {err}")

# Ejemplos de funciones para recuperar datos

def obtener_productos(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return productos

def obtener_clientes(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return clientes


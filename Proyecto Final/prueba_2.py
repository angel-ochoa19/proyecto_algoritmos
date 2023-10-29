import tkinter as tk
from tkinter import ttk
import mysql.connector
from database import conectar_db, cerrar_db

# Conectar a la base de datos
db, cursor = conectar_db()
if db is None:
    exit()

class Producto:
    def _init_(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        # Otros elementos y configuraciones relacionadas con Producto

class Cliente:
    def _init_(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        # Otros elementos y configuraciones relacionadas con Cliente

class Venta:
    def _init_(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        # Otros elementos y configuraciones relacionadas con Venta

# Funciones para controlar la interfaz de usuario
# Función para listar productos y mostrarlos en una tabla
def listar_productos():
    cursor = db.cursor()
    selectQuery = "SELECT * FROM productos"
    cursor.execute(selectQuery)
    productos = cursor.fetchall()
    
    # Crear una nueva ventana para mostrar la tabla de productos
    ventana_productos = tk.Toplevel(root)
    ventana_productos.title("Lista de Productos")
    
    # Crear un Treeview para mostrar la tabla
    tree = ttk.Treeview(ventana_productos, columns=("ID", "Nombre", "Existencia", "Proveedor", "Precio"))
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Nombre")
    tree.heading("#3", text="Existencia")
    tree.heading("#4", text="Proveedor")
    tree.heading("#5", text="Precio")
    
    # Insertar los datos en la tabla
    for producto in productos:
        tree.insert("", "end", values=producto)
    
    tree.pack()
    cursor.close()

# Función para agregar un nuevo producto a la base de datos
def agregar_producto():
    nombre_producto = nombre_producto_entry.get()
    existencia = int(existencia_entry.get())
    proveedor = proveedor_entry.get()
    precio = float(precio_entry.get())

    # Insertar el producto en la base de datos
    query = "INSERT INTO productos (nombre, existencia, proveedor, precio) VALUES (%s, %s, %s, %s)"
    values = (nombre_producto, existencia, proveedor, precio)
    cursor.execute(query, values)
    db.commit()
    print("El producto fue agregado correctamente.")

# Función para borrar un producto de la base de datos
def borrar_producto():
    id_producto = int(id_producto_entry.get())
    query = "DELETE FROM productos WHERE id = %s"
    values = (id_producto,)
    cursor.execute(query, values)
    db.commit()
    print("El producto fue borrado correctamente.")

# Función para listar clientes
def listar_clientes():
    cursor = db.cursor()
    selectQuery = "SELECT * FROM clientes"
    cursor.execute(selectQuery)
    clientes = cursor.fetchall()
    
    # Crear una nueva ventana para mostrar la lista de clientes
    ventana_clientes = tk.Toplevel(root)
    ventana_clientes.title("Lista de Clientes")
    
    # Crear un Treeview para mostrar la lista
    tree = ttk.Treeview(ventana_clientes, columns=("ID", "Nombre", "Email"))
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Nombre")
    tree.heading("#3", text="Email")
    
    # Insertar los datos en la tabla
    for cliente in clientes:
        tree.insert("", "end", values=cliente)
    
    tree.pack()
    cursor.close()

# Función para agregar un nuevo cliente a la base de datos
def agregar_cliente():
    nombre_cliente = nombre_cliente_entry.get()
    email = email_entry.get()

    # Insertar el cliente en la base de datos
    query = "INSERT INTO clientes (nombre, email) VALUES (%s, %s)"
    values = (nombre_cliente, email)
    cursor.execute(query, values)
    db.commit()
    print("El cliente fue agregado correctamente.")

# Función para borrar un cliente de la base de datos
def borrar_cliente():
    id_cliente = int(id_cliente_entry.get())
    query = "DELETE FROM clientes WHERE id = %s"
    values = (id_cliente,)
    cursor.execute(query, values)
    db.commit()
    print("El cliente fue borrado correctamente.")

# Función para listar ventas y mostrarlas en una tabla
def listar_ventas():
    cursor = db.cursor()
    selectQuery = "SELECT * FROM ventas"
    cursor.execute(selectQuery)
    ventas = cursor.fetchall()
    
    # Crear una nueva ventana para mostrar la tabla de ventas
    ventana_ventas = tk.Toplevel(root)
    ventana_ventas.title("Lista de Ventas")
    
    # Crear un Treeview para mostrar la tabla
    tree = ttk.Treeview(ventana_ventas, columns=("ID", "Producto", "Cliente", "Cantidad", "Total"))
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Producto")
    tree.heading("#3", text="Cliente")
    tree.heading("#4", text="Cantidad")
    tree.heading("#5", text="Total")
    
    # Insertar los datos en la tabla
    for venta in ventas:
        tree.insert("", "end", values=venta)
    
    tree.pack()
    cursor.close()

# Función para agregar una nueva venta a la base de datos
def agregar_venta():
    id_producto = int(id_producto_venta_entry.get())
    id_cliente = int(id_cliente_venta_entry.get())
    cantidad = int(cantidad_venta_entry.get())
    total = float(total_venta_entry.get())

    # Insertar la venta en la base de datos
    query = "INSERT INTO ventas (id_producto, id_cliente, cantidad, total) VALUES (%s, %s, %s, %s)"
    values = (id_producto, id_cliente, cantidad, total)
    cursor.execute(query, values)
    db.commit()
    print("La venta fue agregada correctamente.")

# Función para anular una venta de la base de datos
def anular_venta():
    id_venta = int(id_venta_anular_entry.get())
    query = "DELETE FROM ventas WHERE id = %s"
    values = (id_venta,)
    cursor.execute(query, values)
    db.commit()
    print("La venta fue anulada correctamente.")

# Resto del código...

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Sistema de Inventario")
root.geometry("800x500")

# Crear pestañas para diferentes secciones (Inventario, Clientes, Ventas, Reportes)
tab_control = ttk.Notebook(root)

# Pestaña de Inventario
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Inventario')
tab_control.pack(expand=1, fill="both")

# Crear botones y widgets para la pestaña de Inventario
nombre_producto_label = ttk.Label(tab1, text="Nombre del Producto:")
nombre_producto_entry = ttk.Entry(tab1)
existencia_label = ttk.Label(tab1, text="Existencia:")
existencia_entry = ttk.Entry(tab1)
proveedor_label = ttk.Label(tab1, text="Proveedor:")
proveedor_entry = ttk.Entry(tab1)
precio_label = ttk.Label(tab1, text="Precio:")
precio_entry = ttk.Entry(tab1)
agregar_producto_button = ttk.Button(tab1, text="Agregar Producto", command=agregar_producto)
borrar_producto_button = ttk.Button(tab1, text="Borrar Producto", command=borrar_producto)
listar_productos_button = ttk.Button(tab1, text="Listar Productos", command=listar_productos)
id_producto_label = ttk.Label(tab1, text="ID del Producto a Borrar:")
id_producto_entry = ttk.Entry(tab1)

nombre_producto_label.pack()
nombre_producto_entry.pack()
existencia_label.pack()
existencia_entry.pack()
proveedor_label.pack()
proveedor_entry.pack()
precio_label.pack()
precio_entry.pack()
agregar_producto_button.pack()
borrar_producto_button.pack()
listar_productos_button.pack()
id_producto_label.pack()
id_producto_entry.pack()

# Pestaña de Clientes
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Clientes')
tab_control.pack(expand=1, fill="both")

# Crear botones y widgets para la pestaña de Clientes
nombre_cliente_label = ttk.Label(tab2, text="Nombre del Cliente:")
nombre_cliente_entry = ttk.Entry(tab2)
email_label = ttk.Label(tab2, text="Email:")
email_entry = ttk.Entry(tab2)
agregar_cliente_button = ttk.Button(tab2, text="Agregar Cliente", command=agregar_cliente)
borrar_cliente_button = ttk.Button(tab2, text="Borrar Cliente", command=borrar_cliente)
listar_clientes_button = ttk.Button(tab2, text="Listar Clientes", command=listar_clientes)
id_cliente_label = ttk.Label(tab2, text="ID del Cliente a Borrar:")
id_cliente_entry = ttk.Entry(tab2)

nombre_cliente_label.pack()
nombre_cliente_entry.pack()
email_label.pack()
email_entry.pack()
agregar_cliente_button.pack()
borrar_cliente_button.pack()
listar_clientes_button.pack()
id_cliente_label.pack()
id_cliente_entry.pack()

# Pestaña de Ventas
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Ventas')
tab_control.pack(expand=1, fill="both")

# Crear botones y widgets para la pestaña de Ventas
id_producto_venta_label = ttk.Label(tab3, text="ID del Producto:")
id_producto_venta_entry = ttk.Entry(tab3)
id_cliente_venta_label = ttk.Label(tab3, text="ID del Cliente:")
id_cliente_venta_entry = ttk.Entry(tab3)
cantidad_venta_label = ttk.Label(tab3, text="Cantidad:")
cantidad_venta_entry = ttk.Entry(tab3)
total_venta_label = ttk.Label(tab3, text="Total:")
total_venta_entry = ttk.Entry(tab3)
agregar_venta_button = ttk.Button(tab3, text="Agregar Venta", command=agregar_venta)
anular_venta_button = ttk.Button(tab3, text="Anular Venta", command=anular_venta)
listar_ventas_button = ttk.Button(tab3, text="Listar Ventas", command=listar_ventas)
id_venta_anular_label = ttk.Label(tab3, text="ID de Venta a Anular:")
id_venta_anular_entry = ttk.Entry(tab3)

id_producto_venta_label.pack()
id_producto_venta_entry.pack()
id_cliente_venta_label.pack()
id_cliente_venta_entry.pack()
cantidad_venta_label.pack()
cantidad_venta_entry.pack()
total_venta_label.pack()
total_venta_entry.pack()
agregar_venta_button.pack()
anular_venta_button.pack()
listar_ventas_button.pack()
id_venta_anular_label.pack()
id_venta_anular_entry.pack()

# Resto del código...

# Iniciar el bucle principal de Tkinter
root.mainloop()

# Al final del programa, cierra la conexión a la base de datos
cerrar_db(db)
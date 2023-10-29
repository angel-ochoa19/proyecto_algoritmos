-- Crear la base de datos
CREATE DATABASE control_ventas;

-- Usar la base de datos
USE control_ventas;

-- Crear la tabla de productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    precio DECIMAL(10, 2)
);

-- Crear la tabla de clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    email VARCHAR(255)
);

-- Crear la tabla de ventas
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_producto INT,
    codigo_cliente INT,
    cantidad_productos INT,
    total_venta DECIMAL(10, 2)
);

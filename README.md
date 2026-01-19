# Tienda Online – Programación Orientada a Objetos en Python

## Descripción
Este proyecto implementa una tienda online en consola utilizando los principios de la Programación Orientada a Objetos (POO) en Python.  
Permite gestionar productos físicos y digitales, aplicar reglas de negocio y realizar compras desde un menú interactivo.

---

## Objetivo
Aplicar los conceptos de:
- Definición de Clase y Objeto
- Herencia
- Encapsulación
- Polimorfismo

---

## Estructura del Proyecto
---
tienda_online_poo/ 

│

├── main.py # Menú interactivo en consola

├── producto.py # Clase base Producto

├── productos.py # Clases derivadas ProductoFisico y ProductoDigital

├── tienda.py # Gestión del catálogo y compras

└── README.md

## Conceptos de POO Aplicados

### 1Clases y Objetos
- Se define la clase base `Producto` y se crean objetos a partir de ella y de sus clases derivadas.

### Herencia
- `ProductoFisico` y `ProductoDigital` heredan de la clase base `Producto`.

### Encapsulación
- Los atributos `precio` y `stock` son privados y se acceden mediante `@property` y validaciones.
- También se encapsulan atributos específicos como peso, envío y descuento.

### Polimorfismo
- El método `calcular_precio_final()` se sobrescribe en cada clase derivada.
- En el proceso de compra, el sistema llama al método sin importar el tipo real del producto.

---

## Ejecución del Programa
1. Abrir el proyecto en PyCharm.
2. Ejecutar el archivo `main.py`.
3. Usar el menú para:
   - Agregar productos físicos y digitales
   - Listar productos
   - Comprar productos y ver el total

---

## Tecnologías
- Python 3
- Programación Orientada a Objetos
- Consola (CLI)

---
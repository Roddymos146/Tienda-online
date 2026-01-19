# producto.py
# Clase base para representar un producto genérico en una tienda online.
# Aquí demostramos: Definición de clase/objeto y Encapsulación (atributos privados).

class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int):
        # Atributos "normales" (se usan para identificar el producto)
        self.id_producto = id_producto
        self.nombre = nombre

        # Encapsulación: atributos privados (no se deben modificar directamente)
        self.__precio = 0.0
        self.__stock = 0

        # Usamos setters para aplicar validaciones desde el inicio
        self.precio = precio
        self.stock = stock

    # ---------- Encapsulación con @property ----------
    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        self.__precio = float(nuevo_precio)

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = int(nuevo_stock)

    # ---------- Métodos generales ----------
    def vender(self, cantidad: int) -> bool:
        """
        Reduce el stock si hay disponibilidad.
        Retorna True si la venta se realiza, False si no hay stock suficiente.
        """
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return False

        if cantidad > self.stock:
            print("Stock insuficiente.")
            return False

        self.stock -= cantidad
        return True

    def calcular_precio_final(self, cantidad: int) -> float:
        """
        Polimorfismo (base): este método será sobrescrito en las clases derivadas.
        En la clase base, el precio final es simplemente precio * cantidad.
        """
        return self.precio * cantidad

    def mostrar_info(self) -> str:
        return f"ID: {self.id_producto} | {self.nombre} | ${self.precio:.2f} | Stock: {self.stock}"

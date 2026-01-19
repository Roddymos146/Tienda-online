# productos.py
# Clases derivadas para demostrar HERENCIA y POLIMORFISMO.

from producto import Producto


class ProductoFisico(Producto):
    """
    Producto físico: tiene costo de envío (ej. depende del peso).
    Herencia: ProductoFisico hereda de Producto.
    Polimorfismo: sobrescribe calcular_precio_final().
    """

    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int, peso_kg: float, costo_envio: float):
        super().__init__(id_producto, nombre, precio, stock)

        # Encapsulación (opcional extra): atributos privados
        self.__peso_kg = 0.0
        self.__costo_envio = 0.0

        self.peso_kg = peso_kg
        self.costo_envio = costo_envio

    @property
    def peso_kg(self) -> float:
        return self.__peso_kg

    @peso_kg.setter
    def peso_kg(self, nuevo_peso: float):
        if nuevo_peso <= 0:
            raise ValueError("El peso debe ser mayor a 0.")
        self.__peso_kg = float(nuevo_peso)

    @property
    def costo_envio(self) -> float:
        return self.__costo_envio

    @costo_envio.setter
    def costo_envio(self, nuevo_costo: float):
        if nuevo_costo < 0:
            raise ValueError("El costo de envío no puede ser negativo.")
        self.__costo_envio = float(nuevo_costo)

    def calcular_precio_final(self, cantidad: int) -> float:
        """
        Polimorfismo: para productos físicos se suma el costo de envío.
        Regla simple: total = precio*cantidad + (costo_envio * peso_kg)
        """
        if cantidad <= 0:
            return 0.0
        return (self.precio * cantidad) + (self.costo_envio * self.peso_kg)

    def mostrar_info(self) -> str:
        return (
            f"{super().mostrar_info()} | Tipo: Físico | "
            f"Peso: {self.peso_kg}kg | Envío: ${self.costo_envio:.2f}"
        )


class ProductoDigital(Producto):
    """
    Producto digital: no tiene envío, pero puede tener descuento por compra múltiple.
    Herencia: ProductoDigital hereda de Producto.
    Polimorfismo: sobrescribe calcular_precio_final().
    """

    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int, tamanio_mb: float, descuento: float):
        super().__init__(id_producto, nombre, precio, stock)

        # Encapsulación (opcional extra)
        self.__tamanio_mb = 0.0
        self.__descuento = 0.0  # porcentaje, ej. 10 = 10%

        self.tamanio_mb = tamanio_mb
        self.descuento = descuento

    @property
    def tamanio_mb(self) -> float:
        return self.__tamanio_mb

    @tamanio_mb.setter
    def tamanio_mb(self, nuevo_tamanio: float):
        if nuevo_tamanio <= 0:
            raise ValueError("El tamaño (MB) debe ser mayor a 0.")
        self.__tamanio_mb = float(nuevo_tamanio)

    @property
    def descuento(self) -> float:
        return self.__descuento

    @descuento.setter
    def descuento(self, nuevo_descuento: float):
        if not (0 <= nuevo_descuento <= 100):
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.__descuento = float(nuevo_descuento)

    def calcular_precio_final(self, cantidad: int) -> float:
        """
        Polimorfismo: para productos digitales aplicamos un descuento.
        Regla simple: si cantidad >= 3 => aplica descuento (%)
        """
        if cantidad <= 0:
            return 0.0

        total = self.precio * cantidad
        if cantidad >= 3 and self.descuento > 0:
            total -= total * (self.descuento / 100)

        return total

    def mostrar_info(self) -> str:
        return (
            f"{super().mostrar_info()} | Tipo: Digital | "
            f"Tamaño: {self.tamanio_mb}MB | Desc: {self.descuento:.0f}% (>=3)"
        )

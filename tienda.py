# tienda.py
# Clase para gestionar el catálogo y compras (lista, búsqueda, compra).

from typing import List, Optional
from producto import Producto


class Tienda:
    def __init__(self):
        self.productos: List[Producto] = []
        self.__siguiente_id = 1  # encapsulado (control interno de IDs)

    def generar_id(self) -> int:
        id_actual = self.__siguiente_id
        self.__siguiente_id += 1
        return id_actual

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def listar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return

        print("\n--- CATÁLOGO ---")
        for p in self.productos:
            print(p.mostrar_info())

    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        for p in self.productos:
            if p.id_producto == id_producto:
                return p
        return None

    def comprar(self, id_producto: int, cantidad: int) -> float:
        """
        Retorna el total de la compra. Si falla, retorna -1.
        Aquí se ve el polimorfismo porque calcular_precio_final depende del tipo real.
        """
        producto = self.buscar_por_id(id_producto)
        if producto is None:
            print("No existe un producto con ese ID.")
            return -1

        # Venta (valida stock, cantidad)
        if not producto.vender(cantidad):
            return -1

        total = producto.calcular_precio_final(cantidad)  # POLIMORFISMO
        return total

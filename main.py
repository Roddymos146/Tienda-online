# main.py
from tienda import Tienda
from productos import ProductoFisico, ProductoDigital


def leer_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")


def leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debe ser un número (ej. 10.5).")


def menu():
    tienda = Tienda()

    while True:
        print("\n=== TIENDA ONLINE (POO) ===")
        print("1. Agregar producto físico")
        print("2. Agregar producto digital")
        print("3. Listar productos")
        print("4. Comprar producto")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            # Producto físico
            try:
                nombre = input("Nombre: ").strip()
                precio = leer_float("Precio: ")
                stock = leer_int("Stock: ")
                peso = leer_float("Peso (kg): ")
                envio = leer_float("Costo de envío: ")

                nuevo = ProductoFisico(
                    tienda.generar_id(),
                    nombre,
                    precio,
                    stock,
                    peso_kg=peso,
                    costo_envio=envio
                )
                tienda.agregar_producto(nuevo)
                print("✅ Producto físico agregado.")

            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "2":
            # Producto digital
            try:
                nombre = input("Nombre: ").strip()
                precio = leer_float("Precio: ")
                stock = leer_int("Stock: ")
                tamanio = leer_float("Tamaño (MB): ")
                descuento = leer_float("Descuento % (0 a 100): ")

                nuevo = ProductoDigital(
                    tienda.generar_id(),
                    nombre,
                    precio,
                    stock,
                    tamanio_mb=tamanio,
                    descuento=descuento
                )
                tienda.agregar_producto(nuevo)
                print("✅ Producto digital agregado.")

            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "3":
            tienda.listar_productos()

        elif opcion == "4":
            tienda.listar_productos()
            if not tienda.productos:
                continue

            id_producto = leer_int("Ingrese el ID del producto a comprar: ")
            cantidad = leer_int("Cantidad: ")

            total = tienda.comprar(id_producto, cantidad)
            if total != -1:
                print(f"✅ Compra realizada. Total a pagar: ${total:.2f}")

        elif opcion == "5":
            print("Saliendo... 👋")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()

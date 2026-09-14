# Proyecto de Listas - Carrito de Compras
# Materia: Estructuras de Datos
# Alumno: Rodrigo Iglesias
#
# Simula un carrito de compras de una tienda.
# La informacion se guarda en memoria usando LISTAS y el programa
# esta hecho con programacion orientada a objetos.


# ==================== CLASES ====================
class Producto:
    """Un articulo del catalogo de la tienda."""

    def __init__(self, id_producto, nombre, categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


class ItemCarrito:
    """Un producto dentro del carrito junto con la cantidad pedida."""

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        """Formula: subtotal = precio unitario x cantidad"""
        return self.producto.precio * self.cantidad


class Catalogo:
    """Guarda los productos de la tienda en una LISTA."""

    def __init__(self):
        self.productos = [
            Producto(1, "Teclado", "Accesorios", 450),
            Producto(2, "Mouse", "Accesorios", 250),
            Producto(3, "Monitor", "Electronica", 3200),
            Producto(4, "Audifonos", "Audio", 800),
            Producto(5, "Memoria USB", "Almacenamiento", 180),
            Producto(6, "Laptop", "Electronica", 12500),
        ]

    def mostrar(self):
        print("\n=== CATALOGO DE PRODUCTOS ===")
        print("  ID | Producto     | Categoria      | Precio")
        print("  " + "-" * 46)
        for p in self.productos:
            print(f"  {p.id_producto:<3}| {p.nombre:<13}| {p.categoria:<15}| ${p.precio}")

    def buscar(self, dato):
        """Busca un producto por su ID (si se escribe un numero)
        o por su nombre. Regresa el producto o None si no existe."""
        dato = dato.strip()          # quita los espacios de sobra
        for p in self.productos:
            if dato.isdigit() and p.id_producto == int(dato):
                return p
            if p.nombre.lower() == dato.lower():
                return p
        return None


class Carrito:
    """Guarda los productos que el cliente va a comprar en una LISTA."""

    def __init__(self):
        self.items = []

    def buscar(self, dato):
        """Busca un item del carrito por ID o por nombre del producto."""
        dato = dato.strip()          # quita los espacios de sobra
        for item in self.items:
            if dato.isdigit() and item.producto.id_producto == int(dato):
                return item
            if item.producto.nombre.lower() == dato.lower():
                return item
        return None

    def agregar(self, producto, cantidad):
        """Agrega el producto. Si ya estaba en el carrito solo suma la cantidad."""
        item = self.buscar(str(producto.id_producto))
        if item is None:
            self.items.append(ItemCarrito(producto, cantidad))
        else:
            item.cantidad += cantidad

    def total(self):
        """Formula: total = suma de todos los subtotales."""
        suma = 0
        for item in self.items:
            suma += item.subtotal()
        return suma

    def total_articulos(self):
        suma = 0
        for item in self.items:
            suma += item.cantidad
        return suma

    def mostrar(self):
        print("\n=== CARRITO DE COMPRAS ===")
        if len(self.items) == 0:
            print("  El carrito esta vacio.")
            return
        print("  ID | Producto     | Precio | Cant. | Subtotal")
        print("  " + "-" * 48)
        for i in self.items:
            print(f"  {i.producto.id_producto:<3}| {i.producto.nombre:<13}|"
                  f" ${i.producto.precio:<6}| {i.cantidad:<6}| ${i.subtotal()}")
        print("  " + "-" * 48)
        print(f"  TOTAL: ${self.total()}")


# ==================== VALIDACION DE ENTRADAS ====================
def leer_cantidad(mensaje):
    """Pide un numero entero mayor que cero. Si el usuario escribe letras
    o un numero invalido, avisa del error y lo vuelve a pedir."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("  Error: la cantidad debe ser mayor que cero.")
        except ValueError:
            print("  Error: debes escribir un numero.")


def confirmar(mensaje):
    return input(mensaje).strip().lower() in ("s", "si")


# ==================== TIENDA (MENU DEL PROGRAMA) ====================
class Tienda:
    """Une el catalogo con el carrito y controla el menu."""

    def __init__(self):
        self.catalogo = Catalogo()
        self.carrito = Carrito()

    def buscar_producto(self):
        p = self.catalogo.buscar(input("\nID o nombre del producto: "))
        if p is None:
            print("  El producto no existe en el catalogo.")
        else:
            print(f"  ID: {p.id_producto}   Producto: {p.nombre}")
            print(f"  Categoria: {p.categoria}   Precio: ${p.precio}")

    def agregar_producto(self):
        self.catalogo.mostrar()
        p = self.catalogo.buscar(input("\nID o nombre del producto a agregar: "))
        if p is None:
            print("  El producto no existe en el catalogo.")
            return
        print(f"  Producto: {p.nombre}   Precio unitario: ${p.precio}")
        self.carrito.agregar(p, leer_cantidad("  Cantidad: "))
        print("  Producto agregado al carrito!")

    def modificar_cantidad(self):
        self.carrito.mostrar()
        if len(self.carrito.items) == 0:
            return
        item = self.carrito.buscar(input("\nID o nombre del producto a modificar: "))
        if item is None:
            print("  Ese producto no esta en el carrito.")
            return
        print(f"  Producto: {item.producto.nombre}   Cantidad actual: {item.cantidad}")
        item.cantidad = leer_cantidad("  Nueva cantidad: ")
        print("  Cantidad actualizada!")
        print(f"  Nuevo subtotal: ${item.subtotal()}   Nuevo total: ${self.carrito.total()}")

    def eliminar_producto(self):
        self.carrito.mostrar()
        if len(self.carrito.items) == 0:
            return
        item = self.carrito.buscar(input("\nID o nombre del producto a eliminar: "))
        if item is None:
            print("  Ese producto no esta en el carrito.")
            return
        if confirmar(f"  Seguro que desea eliminar {item.producto.nombre}? (s/n): "):
            self.carrito.items.remove(item)
            print("  Producto eliminado del carrito!")
        else:
            print("  Operacion cancelada.")

    def vaciar_carrito(self):
        if len(self.carrito.items) == 0:
            print("\n  El carrito ya esta vacio.")
        elif confirmar("\n  Seguro que desea vaciar el carrito? (s/n): "):
            self.carrito.items = []
            print("  Carrito vaciado!")
        else:
            print("  Operacion cancelada.")

    def finalizar_compra(self):
        if len(self.carrito.items) == 0:
            print("\n  No puede finalizar la compra: el carrito esta vacio.")
            return
        print("\n=== RESUMEN DE COMPRA ===")
        print("  ID | Producto     | Cant. | Subtotal")
        print("  " + "-" * 40)
        for i in self.carrito.items:
            print(f"  {i.producto.id_producto:<3}| {i.producto.nombre:<13}|"
                  f" {i.cantidad:<6}| ${i.subtotal()}")
        print("  " + "-" * 40)
        print(f"  Productos distintos: {len(self.carrito.items)}")
        print(f"  Total de articulos:  {self.carrito.total_articulos()}")
        print(f"  Total a pagar:       ${self.carrito.total()}")
        print("\n  Gracias por su compra!")
        self.carrito.items = []      # la compra se reinicia

    def ejecutar(self):
        """Ciclo principal del programa."""
        while True:
            print("\n=== CARRITO DE COMPRAS ===")
            print("  1. Mostrar catalogo        6. Eliminar producto")
            print("  2. Buscar producto         7. Vaciar carrito")
            print("  3. Agregar al carrito      8. Finalizar compra")
            print("  4. Ver carrito             9. Salir")
            print("  5. Modificar cantidad")
            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                self.catalogo.mostrar()
            elif opcion == "2":
                self.buscar_producto()
            elif opcion == "3":
                self.agregar_producto()
            elif opcion == "4":
                self.carrito.mostrar()
            elif opcion == "5":
                self.modificar_cantidad()
            elif opcion == "6":
                self.eliminar_producto()
            elif opcion == "7":
                self.vaciar_carrito()
            elif opcion == "8":
                self.finalizar_compra()
            elif opcion == "9":
                print("\n  Gracias por usar el programa. Hasta pronto!")
                break
            else:
                print("  Opcion no valida, intente de nuevo.")

            input("\nPresione ENTER para volver al menu...")


# ==================== PROGRAMA PRINCIPAL ====================
tienda = Tienda()
tienda.ejecutar()

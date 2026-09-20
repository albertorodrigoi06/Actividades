


MAXIMO = 10     


# ==================== CLASES ====================
class Pagina:
    """Una pagina web: su direccion y su titulo."""

    def __init__(self, url, titulo):
        self.url = url
        self.titulo = titulo


class Pila:
    """Pila LIFO: el ultimo elemento que entra es el primero que sale."""

    def __init__(self, maximo=MAXIMO):
        self.items = []          # la pila se guarda en una LISTA
        self.maximo = maximo

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.maximo

    def push(self, pagina):
        """Mete una pagina hasta arriba de la pila."""
        self.items.append(pagina)

    def pop(self):
        """Saca y regresa la pagina que esta hasta arriba."""
        return self.items.pop()

    def vaciar(self):
        self.items = []

    def mostrar(self, nombre):
        """Imprime la pila de arriba hacia abajo (primero la cima)."""
        print(f"  {nombre} ({len(self.items)}/{self.maximo}):")
        if self.esta_vacia():
            print("    (vacia)")
            return
        for i in range(len(self.items) - 1, -1, -1):
            marca = "  <- cima" if i == len(self.items) - 1 else ""
            print(f"    {i + 1}. {self.items[i].url}{marca}")


# ==================== TITULOS DE LOS SITIOS ====================
SITIOS = [
    ("https://www.google.com", "Sitio oficial de Google"),
    ("https://www.mozilla.org", "Bienvenido a Mozilla"),
    ("https://openai.com", "Sitio oficial de OpenAI"),
    ("https://stackoverflow.com", "Bienvenido a Stack Overflow"),
    ("https://github.com", "Sitio oficial de GitHub"),
    ("https://merida.anahuac.mx", "Universidad Anahuac Mayab"),
]


def titulo_de(url):
    """Busca el titulo del sitio. Si no lo conoce, regresa uno generico."""
    for direccion, titulo in SITIOS:
        if direccion == url.lower():
            return titulo
    return "Pagina web"


# ==================== NAVEGADOR ====================
class Navegador:
    """Controla la pagina actual y las dos pilas del historial."""

    def __init__(self):
        self.actual = None           # todavia no hay ninguna pagina abierta
        self.atras = Pila()
        self.adelante = Pila()

    def mostrar_pagina_actual(self):
        """La pagina actual se muestra en todo momento."""
        print("\n--- PAGINA ACTUAL ---")
        if self.actual is None:
            print("  (ninguna pagina abierta todavia)")
        else:
            print(f"  {self.actual.url}")
            print(f"  {self.actual.titulo}")

    def visitar(self):
        """Visita una pagina nueva: la actual se guarda en la pila de atras
        y la pila de adelante se vacia."""
        url = input("\nEscriba la URL que desea visitar: ").strip()
        if url == "":
            print("  Aviso: debe escribir una direccion.")
            return
        if self.atras.esta_llena():
            print(f"  Aviso: la pila de retroceso esta llena ({MAXIMO} paginas).")
            print("  Use la opcion Back antes de visitar otra pagina.")
            return

        if self.actual is not None:
            self.atras.push(self.actual)     # la actual pasa al historial
        self.actual = Pagina(url, titulo_de(url))
        self.adelante.vaciar()               # ya no se puede avanzar
        print(f"  Visitando: {self.actual.url}")

    def retroceder(self):
        """Back: la actual se guarda en adelante y se saca la cima de atras."""
        if self.atras.esta_vacia():
            print("\n  Aviso: no hay paginas anteriores para retroceder.")
            return
        self.adelante.push(self.actual)
        self.actual = self.atras.pop()
        print(f"\n  Retrocediendo a: {self.actual.url}")

    def avanzar(self):
        """Forward: la actual se guarda en atras y se saca la cima de adelante."""
        if self.adelante.esta_vacia():
            print("\n  Aviso: no hay paginas siguientes para avanzar.")
            return
        if self.atras.esta_llena():
            print(f"\n  Aviso: la pila de retroceso esta llena ({MAXIMO} paginas).")
            return
        self.atras.push(self.actual)
        self.actual = self.adelante.pop()
        print(f"\n  Avanzando a: {self.actual.url}")

    def mostrar_historial(self):
        print("\n--- HISTORIAL (contenido de las pilas) ---")
        self.atras.mostrar("Pila atras (back)")
        self.adelante.mostrar("Pila adelante (forward)")

    def ejecutar(self):
        """Ciclo principal del programa."""
        print("=== NAVEGADOR WEB (PILAS - LIFO) ===")
        while True:
            self.mostrar_pagina_actual()
            print("\n  1. Visitar una pagina nueva")
            print("  2. Back (retroceder)")
            print("  3. Forward (avanzar)")
            print("  4. Ver el historial")
            print("  5. Exit (salir)")
            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                self.visitar()
            elif opcion == "2":
                self.retroceder()
            elif opcion == "3":
                self.avanzar()
            elif opcion == "4":
                self.mostrar_historial()
            elif opcion == "5":
                print("\n  Gracias por usar el navegador. Hasta pronto!")
                break
            else:
                print("  Opcion no valida, intente de nuevo.")

            input("\nPresione ENTER para continuar...")


# ==================== PROGRAMA PRINCIPAL ====================
navegador = Navegador()
navegador.ejecutar()

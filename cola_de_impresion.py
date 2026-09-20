"""
PROYECTO COLA DE IMPRESIÓN (FIFO - First In, First Out)

Simula una impresora compartida por 5 computadoras (PC1 a PC5).
Los trabajos se agregan al FINAL de la cola y se imprimen desde el FRENTE,
respetando el orden de llegada.

La cola se implementa con un arreglo (lista de Python) de capacidad fija.
Versión de consola (CLI).
"""

import random

# ----------------------------------------------------------------------
# Constantes del sistema
# ----------------------------------------------------------------------
CAPACIDAD_MAXIMA = 6
COMPUTADORAS = ["PC1", "PC2", "PC3", "PC4", "PC5"]


# ======================================================================
# CLASE: TrabajoImpresion
# ----------------------------------------------------------------------
# Atributos: numero, computadora
# Métodos:   __str__()
# ======================================================================
class TrabajoImpresion:
    """Representa un documento enviado a imprimir por una computadora."""

    def __init__(self, numero, computadora):
        self.numero = numero            # Número consecutivo del trabajo
        self.computadora = computadora  # PC que envió el documento

    def __str__(self):
        return f"{self.computadora} (trabajo #{self.numero})"


# ======================================================================
# CLASE: ColaImpresion
# ----------------------------------------------------------------------
# Atributos: capacidad, elementos, contador_trabajos
# Métodos:   esta_vacia(), esta_llena(), encolar(), desencolar(),
#            frente(), tamanio(), mostrar()
# ======================================================================
class ColaImpresion:
    """Estructura de datos Cola (FIFO) con capacidad máxima."""

    def __init__(self, capacidad=CAPACIDAD_MAXIMA):
        self.capacidad = capacidad
        self.elementos = []          # Arreglo que guarda los trabajos
        self.contador_trabajos = 0   # Para numerar cada trabajo

    def esta_vacia(self):
        """R5 - Verifica si la cola no tiene trabajos pendientes."""
        return len(self.elementos) == 0

    def esta_llena(self):
        """R4 - Verifica si la cola alcanzó su capacidad máxima."""
        return len(self.elementos) == self.capacidad

    def encolar(self, computadora):
        """
        R1 - Agrega un trabajo al FINAL de la cola.
        Devuelve el trabajo agregado, o None si la cola está llena.
        """
        if self.esta_llena():
            return None
        self.contador_trabajos += 1
        trabajo = TrabajoImpresion(self.contador_trabajos, computadora)
        self.elementos.append(trabajo)   # Inserción al final
        return trabajo

    def desencolar(self):
        """
        R2 - Elimina y devuelve el trabajo del FRENTE de la cola.
        Devuelve None si la cola está vacía.
        """
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)     # Eliminación del primero

    def frente(self):
        """Devuelve el primer trabajo sin eliminarlo."""
        if self.esta_vacia():
            return None
        return self.elementos[0]

    def tamanio(self):
        """Cantidad de trabajos pendientes."""
        return len(self.elementos)

    def mostrar(self):
        """R3 - Devuelve la lista de trabajos pendientes en orden de atención."""
        return list(self.elementos)


# ======================================================================
# CLASE: SistemaImpresion (interfaz de consola)
# ----------------------------------------------------------------------
# Atributos: cola
# Métodos:   agregar_trabajo(), imprimir_documento(), mostrar_cola(),
#            menu(), ejecutar()
# ======================================================================
class SistemaImpresion:
    """Maneja el menú por consola y las operaciones sobre la cola."""

    def __init__(self):
        self.cola = ColaImpresion()

    # ------------------------------------------------------------------
    # Requerimientos funcionales
    # ------------------------------------------------------------------
    def agregar_trabajo(self):
        """R1 y R4 - Una PC aleatoria envía un documento a la cola."""
        computadora = random.choice(COMPUTADORAS)
        print(f"\n{computadora} envía un documento a imprimir...")

        if self.cola.esta_llena():
            print("La cola de impresión está LLENA")
        else:
            trabajo = self.cola.encolar(computadora)
            print(f"Trabajo agregado al final de la cola: {trabajo}")

        self.mostrar_cola()

    def imprimir_documento(self):
        """R2 y R5 - Imprime (elimina) el primer trabajo de la cola."""
        if self.cola.esta_vacia():
            print("\nLa cola de impresión está VACÍA")
            return

        trabajo = self.cola.desencolar()
        print(f"\nImprimiendo documento de {trabajo.computadora}...")
        print(f"Impresión {trabajo} finalizada")
        self.mostrar_cola()

    def mostrar_cola(self):
        """R3 - Muestra los trabajos pendientes en orden de atención."""
        if self.cola.esta_vacia():
            print("Cola de impresión: (vacía)")
            return

        print(f"Cola de impresión ({self.cola.tamanio()}/{self.cola.capacidad}):")
        for posicion, trabajo in enumerate(self.cola.mostrar(), start=1):
            marca = "  <- se imprime primero" if posicion == 1 else ""
            print(f"  {posicion}. {trabajo}{marca}")

    # ------------------------------------------------------------------
    # Menú principal
    # ------------------------------------------------------------------
    def menu(self):
        print("\n===== COLA DE IMPRESIÓN (FIFO) =====")
        print("1. Agregar trabajo de impresión")
        print("2. Imprimir documento")
        print("3. Mostrar cola de impresión")
        print("4. Salir")

    def ejecutar(self):
        """Ciclo principal del programa."""
        opcion = ""
        while opcion != "4":
            self.menu()
            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                self.agregar_trabajo()
            elif opcion == "2":
                self.imprimir_documento()
            elif opcion == "3":
                print()
                self.mostrar_cola()
            elif opcion == "4":
                print("\nPrograma finalizado.")
            else:
                print("\nOpción inválida. Elija un número del 1 al 4.")


# ======================================================================
# Programa principal
# ======================================================================
if __name__ == "__main__":
    SistemaImpresion().ejecutar()



import random


# ==========================================================
# CLASE Resistencia
# Representa una sola resistencia con su valor en ohmios.
# ==========================================================
class Resistencia:

    # arreglo con el nombre de cada color
    # la posicion dentro del arreglo es el numero que vale el color
    NOMBRES = ["Negro", "Marron", "Rojo", "Naranja", "Amarillo",
               "Verde", "Azul", "Violeta", "Gris", "Blanco"]

    def __init__(self, valor):
        # atributo de la clase: el valor de la resistencia en ohmios
        self.valor = valor

    def obtener_indices(self):
        """Regresa un arreglo con los 3 numeros de las bandas."""
        texto = str(self.valor)
        primer_digito = int(texto[0])       # primera banda
        segundo_digito = int(texto[1])      # segunda banda
        multiplicador = len(texto) - 2      # tercera banda (ceros que sobran)
        return [primer_digito, segundo_digito, multiplicador]

    def obtener_colores(self):
        """Regresa un arreglo con los 3 nombres de color."""
        indices = self.obtener_indices()
        colores = []
        for i in range(3):
            colores.append(Resistencia.NOMBRES[indices[i]])
        return colores

    def mostrar_colores(self):
        """Imprime en pantalla las tres bandas de la resistencia."""
        colores = self.obtener_colores()
        print("Valor:", self.valor, "ohms")
        print("Primera banda (primer digito) :", colores[0])
        print("Segunda banda (segundo digito):", colores[1])
        print("Tercera banda (multiplicador) :", colores[2])


# ==========================================================
# CLASE ArregloResistencias  (clase padre)
# Guarda un arreglo de n resistencias con valores aleatorios.
# ==========================================================
class ArregloResistencias:

    def __init__(self, n):
        self.n = n                  # cuantas resistencias son
        self.resistencias = []      # el arreglo donde se guardan
        self.generar()

    def generar(self):
        """Llena el arreglo con n valores aleatorios entre 10 y 1000000000."""
        self.resistencias = []
        for i in range(self.n):
            valor = random.randint(10, 1000000000)
            self.resistencias.append(Resistencia(valor))

    def mostrar(self):
        """Imprime cada resistencia del arreglo."""
        for i in range(self.n):
            print("R" + str(i + 1) + " = " +
                  str(self.resistencias[i].valor) + " ohms")

    def calcular_total(self):
        """Las clases hijas son las que dicen como se calcula."""
        return 0


# ==========================================================
# CLASE ArregloSerie  (hereda de ArregloResistencias)
# Rts = R1 + R2 + R3 + ... + RN
# ==========================================================
class ArregloSerie(ArregloResistencias):

    def calcular_total(self):
        total = 0
        for i in range(self.n):
            total = total + self.resistencias[i].valor
        return total


# ==========================================================
# CLASE ArregloParalelo  (hereda de ArregloResistencias)
# 1/Rtp = 1/R1 + 1/R2 + 1/R3 + ... + 1/RN
# ==========================================================
class ArregloParalelo(ArregloResistencias):

    def calcular_total(self):
        suma = 0.0
        for i in range(self.n):
            suma = suma + (1.0 / self.resistencias[i].valor)
        return 1.0 / suma


# ==========================================================
# CLASE Aplicacion
# Se encarga del menu y de pedirle los datos al usuario.
# ==========================================================
class Aplicacion:

    def opcion_colores(self):
        """Requerimiento 1: del valor saca los colores."""
        print()
        valor = int(input("Escribe el valor de la resistencia en ohms: "))

        if valor < 10:
            print("El valor debe ser de al menos 10 ohms.")
            return

        resistencia = Resistencia(valor)
        print()
        resistencia.mostrar_colores()

    def opcion_serie(self):
        """Requerimiento 2: total de n resistencias en serie."""
        print()
        n = int(input("Cuantas resistencias en serie quieres? "))

        arreglo = ArregloSerie(n)
        print()
        arreglo.mostrar()

        total = arreglo.calcular_total()
        print()
        print("Resistencia total en SERIE = " + str(total) + " ohms")

    def opcion_paralelo(self):
        """Requerimiento 3: total de n resistencias en paralelo."""
        print()
        n = int(input("Cuantas resistencias en paralelo quieres? "))

        arreglo = ArregloParalelo(n)
        print()
        arreglo.mostrar()

        total = arreglo.calcular_total()
        print()
        print("Resistencia total en PARALELO = " + str(round(total, 4)) + " ohms")

    def menu(self):
        """Muestra el menu y repite hasta que el usuario sale."""
        salir = False
        while salir == False:
            print()
            print("===== PROYECTO RESISTENCIA ELECTRICA =====")
            print("1. Sacar los colores de una resistencia")
            print("2. Resistencias en serie")
            print("3. Resistencias en paralelo")
            print("4. Salir")

            opcion = input("Elige una opcion: ")

            if opcion == "1":
                self.opcion_colores()
            elif opcion == "2":
                self.opcion_serie()
            elif opcion == "3":
                self.opcion_paralelo()
            elif opcion == "4":
                print("Adios.")
                salir = True
            else:
                print("Esa opcion no existe.")


# ---------- AQUI EMPIEZA EL PROGRAMA ----------
app = Aplicacion()
app.menu()

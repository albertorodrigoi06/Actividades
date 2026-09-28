
class Nodo:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, info):
        nuevo = Nodo(info)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        padre = None

        while actual is not None:
            padre = actual
            if info < actual.info:
                actual = actual.izq
            else:
                actual = actual.der

        if info < padre.info:
            padre.izq = nuevo
        else:
            padre.der = nuevo



if __name__ == "__main__":
    arbol = ArbolBinario()
    cantidad = int(input("Ingrese la cantidad de nodos a insertar: "))
    for i in range(cantidad):
        valor = int(input(f"Ingrese el valor del nodo {i + 1}: "))
        arbol.insertar(valor)

    def inorden(nodo):
        if nodo is not None:
            inorden(nodo.izq)
            print(nodo.info, end=" ")
            inorden(nodo.der)

    print("Inorden:")
    inorden(arbol.raiz)
    print()

    def preorden(nodo):
        if nodo is not None:
            print(nodo.info, end=" ")
            preorden(nodo.izq)
            preorden(nodo.der)
    print("Preorden: ")
    preorden(arbol.raiz)
    print()

    def posorden(nodo):
        if nodo is not None:
            posorden(nodo.izq)
            posorden(nodo.der)
            print(nodo.info, end=" ")

    print("Posorden: ")
    posorden(arbol.raiz)
    print()

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

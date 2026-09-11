lista_impresion = []
codigo_actual = 1


def registrar_documento(codigo):
    archivo = input("Ingrese el nombre del archivo: ")
    cantidad_paginas = int(input("Ingrese la cantidad de páginas: "))

    nuevo_documento = {
        "codigo": codigo,
        "archivo": archivo,
        "cantidad": cantidad_paginas
    }

    lista_impresion.append(nuevo_documento)

    print("Documento registrado correctamente.")
    print("Código asignado:", codigo)

    return codigo + 1


def imprimir_siguiente():
    if not lista_impresion:
        print("No existen documentos pendientes.")
        return

    documento = lista_impresion.pop(0)

    print("\n--- IMPRIMIENDO ---")
    print("Archivo:", documento["archivo"])
    print("Cantidad de páginas:", documento["cantidad"])
    print("Código:", documento["codigo"])
    print("Impresión finalizada.")


def consultar_pendientes():
    if not lista_impresion:
        print("Actualmente no hay documentos pendientes.")
        return

    print("\n--- COLA ACTUAL ---")

    for indice, documento in enumerate(lista_impresion, start=1):
        print(
            indice,
            "- Código:", documento["codigo"],
            "| Archivo:", documento["archivo"],
            "| Páginas:", documento["cantidad"]
        )


def menu_principal():
    print("\n===== SISTEMA DE IMPRESIÓN =====")
    print("1. Registrar documento")
    print("2. Imprimir siguiente documento")
    print("3. Mostrar documentos pendientes")
    print("4. Finalizar programa")


seleccion = 0

while seleccion != 4:

    menu_principal()
    seleccion = int(input("Seleccione una opción: "))

    if seleccion == 1:
        codigo_actual = registrar_documento(codigo_actual)

    elif seleccion == 2:
        imprimir_siguiente()

    elif seleccion == 3:
        consultar_pendientes()

    elif seleccion == 4:
        print("Programa finalizado.")

    else:
        print("La opción ingresada no es válida.")
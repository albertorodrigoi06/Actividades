

archivo = open('romeo.txt', 'w')
archivo.write('But soft what light through yonder window breaks\n')
archivo.write('It is the east and Juliet is the sun\n')
archivo.write('Arise fair sun and kill the envious moon\n')
archivo.write('Who is already sick and pale with grief\n')
archivo.close()

archivo = open('mbox.txt', 'w')
archivo.write('From rodrigo@anahuac.mx Mon Aug 24 08:14:16 2026\n')
archivo.write('Subject: Entrega P1A4\n')
archivo.write('From ana@anahuac.mx Mon Aug 24 09:02:41 2026\n')
archivo.write('Subject: Duda sobre listas\n')
archivo.write('From luis@anahuac.mx Tue Aug 25 11:37:05 2026\n')
archivo.write('Subject: Rebanado de listas\n')
archivo.write('From ana@anahuac.mx Wed Aug 26 16:45:52 2026\n')
archivo.write('Subject: Ejercicio 5 resuelto\n')
archivo.close()


# ---------- EJERCICIO 4 ----------

print('EJERCICIO 4')

manejador = open('romeo.txt')
lista = []

for linea in manejador:
    palabras = linea.split()
    for palabra in palabras:
        if palabra not in lista:
            lista.append(palabra)

lista.sort()
print(lista)


# ---------- EJERCICIO 5 ----------

print()
print('EJERCICIO 5')

manejador = open('mbox.txt')
contador = 0

for linea in manejador:
    if linea.startswith('From '):
        palabras = linea.split()
        print(palabras[1])
        contador = contador + 1

print('Hubo', contador, 'lineas en el archivo con From como primera palabra')

def sumatoria_cuadrados(n):
    if n == 0:
        return 0
    else:
        return (n * n) + sumatoria_cuadrados(n - 1)


num = int(input("Ingresa un numero entero positivo (menor o igual a 50): "))

if num > 0 and num <= 50:
    resultado = sumatoria_cuadrados(num)
    print("La sumatoria de los primeros", num, "numeros al cuadrado es:", resultado)
else:
    print("El numero debe ser mayor a 0 y menor o igual a 50")
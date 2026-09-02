def calcular_capital(m, x, n):
    if n == 0:
        return m
    else:
        return calcular_capital(m, x, n - 1) * (1 + x / 100)


capital_inicial = float(input("Ingresa el capital inicial (m): "))
tasa_interes = float(input("Ingresa la tasa de interes anual (X%): "))
anios = int(input("Ingresa el numero de años: "))

capital_final = calcular_capital(capital_inicial, tasa_interes, anios)
print("El capital al cabo de", anios, "años sera:", capital_final)
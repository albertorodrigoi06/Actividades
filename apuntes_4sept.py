def esta_balanceada(expresion):
    
    pila = []
    
    
    for letra in expresion:
        if letra == "()":
            pila.append(letra)
        elif letra == ")":
            pila.pop()
        return len(pila) == 0
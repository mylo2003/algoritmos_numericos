def metodo_secante(func, x0, x1, tol):
    """
    Método de la Secante para encontrar las raíces de una función continua.
    
    Parámetros:
    func: La función para la cual estamos buscando la raíz.
    x0: Primera aproximación inicial.
    x1: Segunda aproximación inicial.
    tol: Tolerancia para el criterio de convergencia.
    
    Retorna:
    Una aproximación de la raíz de la función.
    """
    iteraciones = 0
    errores_e_iteraciones = []
    error_actual = 100

    while abs(error_actual) >= tol:
        iteraciones += 1
        if abs(func(x1) - func(x0)) < 1e-15:  # Evitar división por cero
            print("La diferencia entre f(x1) y f(x0) es muy pequeña, posible división por cero.")
            return None
        
        x2 = x1 - (((x1 - x0) / (func(x1) - func(x0))) * func(x1))

        error_actual = abs(x2 - x1)
        errores_e_iteraciones.append((iteraciones, error_actual))

        x0, x1 = x1, x2
        
    return x1, errores_e_iteraciones

if __name__ == "__main__":
    import sympy as sp
    
    # Solicitar la función al usuario
    funcion_str = input("Ingresa la función en términos de x (por ejemplo, x**3 - x - 2): ")
    
    # Convertir la función de string a una función usable en Python
    x = sp.symbols('x')
    funcion = sp.sympify(funcion_str)
    func = sp.lambdify(x, funcion)
    
    # Solicitar las aproximaciones iniciales y la tolerancia
    x0 = float(input("Ingresa la primera aproximación inicial (x0): "))
    x1 = float(input("Ingresa la segunda aproximación inicial (x1): "))
    tol = float(input("Ingresa la tolerancia (por ejemplo, 1e-6): "))
    
    # Encontrar la raíz usando el método de la secante
    raiz = metodo_secante(func, x0, x1, tol)
    if raiz is not None:
        print(f"La raíz aproximada es: {raiz}")

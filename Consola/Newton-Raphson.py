def metodo_newton_raphson(func, dfunc, x0, tol):
    """
    Método de Newton-Raphson para encontrar las raíces de una función continua.
    
    Parámetros:
    func: La función para la cual estamos buscando la raíz.
    dfunc: La derivada de la función.
    x0: Aproximación inicial.
    tol: Tolerancia para el criterio de convergencia.
    
    Retorna:
    Una aproximación de la raíz de la función.
    """
    iteraciones = 0
    errores_e_iteraciones = []
    error_actual =  100

    while error_actual >= tol:
        if abs(dfunc(x0)) < 1e-15:  # Evitar división por cero
            print("La derivada en el punto es muy pequeña, posible división por cero.")
            return None
        
        x1 = x0 - func(x0) / dfunc(x0)

        error_actual = abs((x1 - x0) / x1)
        errores_e_iteraciones.append((iteraciones, error_actual))

        x0 = x1
        
    return x0, errores_e_iteraciones


if __name__ == "__main__":
    import sympy as sp
    
    # Solicitar la función al usuario
    funcion_str = input("Ingresa la función en términos de x (por ejemplo, x**3 - x - 2): ")
    
    # Convertir la función de string a una función usable en Python
    x = sp.symbols('x')
    funcion = sp.sympify(funcion_str)
    dfuncion = sp.diff(funcion, x)  # Derivada de la función
    func = sp.lambdify(x, funcion)
    dfunc = sp.lambdify(x, dfuncion)
    
    # Solicitar la aproximación inicial y la tolerancia
    x0 = float(input("Ingresa la aproximación inicial (x0): "))
    tol = float(input("Ingresa la tolerancia (por ejemplo, 1e-6): "))
    
    # Encontrar la raíz usando el método de Newton-Raphson
    raiz = metodo_newton_raphson(func, dfunc, x0, tol)
    if raiz is not None:
        print(f"La raíz aproximada es: {raiz}")

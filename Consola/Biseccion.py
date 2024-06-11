def metodo_biseccion(func, a, b, tol):
  """
  Método de Bisección para encontrar las raíces de una función continua en un intervalo [a, b].
  
  Parámetros:
  func: La función para la cual estamos buscando la raíz.
  a: Límite inferior del intervalo.
  b: Límite superior del intervalo.
  tol: Tolerancia para el criterio de convergencia.
  
  Retorna:
  Una aproximación de la raíz de la función en el intervalo [a, b].
  """
  
  if func(a) * func(b) >= 0:
    print("El método de bisección no puede aplicarse, ya que no hay un cambio de signo en el intervalo.")
    return None
  
  c = a
  iteraciones = 0
  errores_e_iteraciones = []
  error_actual = 100
  
  while error_actual > tol:
    iteraciones += 1
    c = (a + b) / 2.0
    error_actual = (b - a)/2.0
    errores_e_iteraciones.append((iteraciones, error_actual))
    if func(c) == 0:  # Encontramos la raíz exacta
      break
    if func(a) * func(c) < 0:
      b = c
    else:
      a = c
          
  return c, errores_e_iteraciones


if __name__ == "__main__":
  import sympy as sp
  
  # Solicitar la función al usuario
  funcion_str = input("Ingresa la función en términos de x (por ejemplo, x**3 - x - 2): ")
  
  # Convertir la función de string a una función usable en Python
  x = sp.symbols('x')
  funcion = sp.sympify(funcion_str)
  func = sp.lambdify(x, funcion)
  
  # Solicitar los límites del intervalo y la tolerancia
  a = float(input("Ingresa el límite inferior del intervalo (a): "))
  b = float(input("Ingresa el límite superior del intervalo (b): "))
  tol = float(input("Ingresa la tolerancia (por ejemplo, 1e-6): "))
  
  # Encontrar la raíz usando el método de bisección
  raiz = metodo_biseccion(func, a, b, tol)
  if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")

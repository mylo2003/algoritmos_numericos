import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


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
        messagebox.showerror("Error", "El método de bisección no puede aplicarse, ya que no hay un cambio de signo en el intervalo.")
        return None
    
    c = a
    iteraciones = 0
    errores_e_iteraciones = []
    error_actual = 100
    
    while error_actual > tol:
        iteraciones += 1
        c = (a + b) / 2.0
        error_actual = (b - a) / 2.0
        errores_e_iteraciones.append((iteraciones, error_actual))
        if func(c) == 0:  # Encontramos la raíz exacta
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    
    # Graficar el progreso
    plt.plot([iteracion[0] for iteracion in errores_e_iteraciones], 
             [error[1] for error in errores_e_iteraciones], 
             marker='o', linestyle='-')
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.title('Progreso del método de bisección')
    plt.grid(True)
    plt.tight_layout()
    
    return c, errores_e_iteraciones


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
            messagebox.showerror("Error", "La diferencia entre f(x1) y f(x0) es muy pequeña, posible división por cero.")
            return None
        
        x2 = x1 - (((x1 - x0) / (func(x1) - func(x0))) * func(x1))

        error_actual = abs(x2 - x1)
        errores_e_iteraciones.append((iteraciones, error_actual))

        x0, x1 = x1, x2
    
    # Graficar el progreso
    plt.plot([iteracion[0] for iteracion in errores_e_iteraciones], 
             [error[1] for error in errores_e_iteraciones], 
             marker='o', linestyle='-')
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.title('Progreso del método de la secante')
    plt.grid(True)
    plt.tight_layout()
    
    return x1, errores_e_iteraciones


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
            messagebox.showerror("Error", "La derivada en el punto es muy pequeña, posible división por cero.")
            return None
        
        x1 = x0 - func(x0) / dfunc(x0)

        error_actual = abs((x1 - x0) / x1)
        errores_e_iteraciones.append((iteraciones, error_actual))

        x0 = x1
    
    # Graficar el progreso
    plt.plot([iteracion[0] for iteracion in errores_e_iteraciones], 
             [error[1] for error in errores_e_iteraciones], 
             marker='o', linestyle='-')
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.title('Progreso del método de Newton-Raphson')
    plt.grid(True)
    plt.tight_layout()
    
    return x0, errores_e_iteraciones


def mostrar_parametros(metodo):
    if metodo == "Bisección":
        a_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        a_entry.grid(row=1, column=1, padx=5, pady=5)
        b_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
        b_entry.grid(row=2, column=1, padx=5, pady=5)
        x0_label.grid_remove()
        x0_entry.grid_remove()
        x1_label.grid_remove()
        x1_entry.grid_remove()
    elif metodo == "Secante":
        a_label.grid_remove()
        a_entry.grid_remove()
        b_label.grid_remove()
        b_entry.grid_remove()
        x0_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        x0_entry.grid(row=1, column=1, padx=5, pady=5)
        x1_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
        x1_entry.grid(row=2, column=1, padx=5, pady=5)
    else:
        a_label.grid_remove()
        a_entry.grid_remove()
        b_label.grid_remove()
        b_entry.grid_remove()
        x0_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        x0_entry.grid(row=1, column=1, padx=5, pady=5)
        x1_label.grid_remove()
        x1_entry.grid_remove()


def calcular():
    funcion_str = funcion_entry.get()
    tol = float(tol_entry.get())
    
    x = sp.symbols('x')
    funcion = sp.sympify(funcion_str)
    dfuncion = sp.diff(funcion, x)
    func = sp.lambdify(x, funcion)
    dfunc = sp.lambdify(x, dfuncion)
    
    metodo = metodo_combobox.get()
    if metodo == "Bisección":
        a = float(a_entry.get())
        b = float(b_entry.get())
        raiz = metodo_biseccion(func, a, b, tol)
    elif metodo == "Secante":
        x0 = float(x0_entry.get())
        x1 = float(x1_entry.get())
        raiz = metodo_secante(func, x0, x1, tol)
    else:
        x0 = float(x0_entry.get())
        raiz = metodo_newton_raphson(func, dfunc, x0, tol)
    
    if raiz is not None:
        resultado_label.config(text=f"La raíz aproximada es: {raiz[0]}")

        # Crear y mostrar la gráfica en la interfaz
        figure = plt.figure(figsize=(6, 4))
        canvas = FigureCanvasTkAgg(figure, master=grafica_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Actualizar la gráfica con los datos del método seleccionado
        if metodo == "Bisección":
            graficar_biseccion(figure, raiz[1])
        elif metodo == "Secante":
            graficar_secante(figure, raiz[1])
        else:
            graficar_newton_raphson(figure, raiz[1])

        grafica_frame.update()


def graficar_biseccion(figure, data):
    ax = figure.add_subplot(111)
    ax.plot([iteracion[0] for iteracion in data], 
            [error[1] for error in data], 
            marker='o', linestyle='-')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Error')
    ax.set_title('Progreso del método de bisección')
    ax.grid(True)
    ax.tight_layout()


def graficar_secante(figure, data):
    ax = figure.add_subplot(111)
    ax.plot([iteracion[0] for iteracion in data], 
            [error[1] for error in data], 
            marker='o', linestyle='-')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Error')
    ax.set_title('Progreso del método de la secante')
    ax.grid(True)
    ax.tight_layout()


def graficar_newton_raphson(figure, data):
    ax = figure.add_subplot(111)
    ax.plot([iteracion[0] for iteracion in data], 
            [error[1] for error in data], 
            marker='o', linestyle='-')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Error')
    ax.set_title('Progreso del método de Newton-Raphson')
    ax.grid(True)
    ax.tight_layout()


# Crear la ventana principal
root = tk.Tk()
root.title("Métodos Numéricos")

# Frame para los métodos numéricos
metodos_frame = ttk.LabelFrame(root, text="Métodos Numéricos")
metodos_frame.grid(row=0, column=0, padx=10, pady=10)

# Crear widgets dentro del frame
metodo_label = ttk.Label(metodos_frame, text="Selecciona el método:")
metodo_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

metodo_combobox = ttk.Combobox(metodos_frame, values=["Bisección", "Secante", "Newton-Raphson"], 
                               state="readonly", width=20)
metodo_combobox.grid(row=0, column=1, padx=5, pady=5)
metodo_combobox.current(0)
metodo_combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_parametros(metodo_combobox.get()))

# Frame para los parámetros
parametros_frame = ttk.LabelFrame(root, text="Parámetros")
parametros_frame.grid(row=1, column=0, padx=10, pady=10)

# Crear widgets dentro del frame
funcion_label = ttk.Label(parametros_frame, text="Función (f(x)):")
funcion_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

funcion_entry = ttk.Entry(parametros_frame, width=30)
funcion_entry.grid(row=0, column=1, padx=5, pady=5)

a_label = ttk.Label(parametros_frame, text="Límite inferior (a):")
a_entry = ttk.Entry(parametros_frame, width=10)

b_label = ttk.Label(parametros_frame, text="Límite superior (b):")
b_entry = ttk.Entry(parametros_frame, width=10)

x0_label = ttk.Label(parametros_frame, text="Aprox. inicial (x0):")
x0_entry = ttk.Entry(parametros_frame, width=10)

x1_label = ttk.Label(parametros_frame, text="Aprox. inicial (x1):")
x1_entry = ttk.Entry(parametros_frame, width=10)

tol_label = ttk.Label(parametros_frame, text="Tolerancia:")
tol_entry = ttk.Entry(parametros_frame, width=10)
tol_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")
tol_entry.grid(row=5, column=1, padx=5, pady=5)

# Botón para calcular
calcular_button = ttk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=2, column=0, padx=10, pady=10)

# Frame para la gráfica
grafica_frame = ttk.LabelFrame(root, text="Gráfica")
grafica_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

# Resultado
resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()

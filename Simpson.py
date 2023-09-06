import math
import numpy as np
import matplotlib.pyplot as plt

def metodo_simpson(funcion, a, b, n):
    h = (b - a) / n
    integral = funcion(a) + funcion(b)

    for i in range(1, n):
        x_i = a + i * h
        coef = 4 if i % 2 == 1 else 2
        integral += coef * funcion(x_i)

    integral *= h / 3
    return integral

# Definir la función e^(x^4)
def funcion_ejemplo(x):
    return math.exp(x**4)

# Definir el intervalo y el número de puntos para la gráfica
a = -1
b = 1
n = 1000

# Crear un arreglo de valores de x en el intervalo
x_values = np.linspace(a, b, n)

# Calcular los valores correspondientes de y para la función
y_values = [funcion_ejemplo(x) for x in x_values]

# Graficar la función
plt.plot(x_values, y_values, label='e^(x^4)')
plt.fill_between(x_values, 0, y_values, alpha=0.2)

# Calcular la integral utilizando el método de Simpson
resultado = metodo_simpson(funcion_ejemplo, a, b, n)
print(f"Aproximación de la integral definida: {resultado}")

# Mostrar la aproximación en la gráfica
plt.axhline(resultado, color='red', linestyle='--', label='Aproximación de la integral')
plt.legend()

# Etiquetas y título de la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de e^(x^4) y Aproximación de la Integral (Método de Simpson)')

# Mostrar la gráfica
plt.grid()
plt.show()
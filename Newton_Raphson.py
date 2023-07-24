import numpy as np
import matplotlib.pyplot as plt

# Funciones
def funcion(x):
    return x**3 + 2*x**2 + 10*x - 20

def funcion_derivada(x):
    return 3*x**2 + 4*x + 10

def error(valor1, valor2):
    resultado = abs(((valor1 - valor2) / valor1) * 100)
    return resultado

# Procedimiento
def metodoNewtonRaphson():
    global raiz, puntos
    puntos = []
    raiz = 0
    contador = 0
    xi = 1  # Puedes cambiar el valor inicial aquí
    max_iter = 100  # Número máximo de iteraciones permitidas
    tol = 1e-6  # Tolerancia para la convergencia

    while contador < max_iter:
        xr = xi - funcion(xi) / funcion_derivada(xi)
        fxr = round(funcion(xr), 5)
        valorError = error(raiz, xr)
        print("i ", contador + 1, " xr=", xr, " f(xr)=", fxr)
        xi = xr
        contador += 1
        raiz = xr
        puntos.append(raiz)

        if valorError <= tol:
            print("El resultado de f(x) se acerca a cero. Converge a la raiz.")
            break
    print("El valor del error es de.", valorError)

metodoNewtonRaphson()

# Salida
# Graficas
x = np.linspace(-5, 5, 100)
y = funcion(x)

plt.plot(x, y, 'b')
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
plt.scatter(raiz, 0, color='red')
for i in range(len(puntos)):
    plt.scatter(puntos[i], 0, color='green', s=10)
plt.ylim(-30, 30)  # Ajustar el límite del eje y
plt.title('Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()
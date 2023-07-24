import numpy as np
import matplotlib.pyplot as plt

# Funciones
def funcion(x):
    return x**3 + 2*x**2 + 10*x - 20

def error(valor1, valor2):
    resultado = abs(((valor1 - valor2) / valor1) * 100)
    return resultado

# Procedimiento
def metodoSecante():
    global raiz, puntos
    puntos = []
    raiz = 0
    contador = 0
    x0 = 1  # Valor inicial 1
    x1 = 2  # Valor inicial 2
    max_iter = 100  # Número máximo de iteraciones permitidas
    tol = 1e-6  # Tolerancia para la convergencia

    while contador < max_iter:
        xr = x1 - funcion(x1) * (x1 - x0) / (funcion(x1) - funcion(x0))
        fxr = round(funcion(xr), 5)
        valorError = error(raiz, xr)
        print("i ", contador + 1, " xr=", xr, " f(xr)=", fxr)
        x0 = x1
        x1 = xr
        contador += 1
        raiz = xr
        puntos.append(raiz)

        if valorError <= tol:
            print("El resultado de f(x) se acerca a cero. Converge a la raiz.")
            break
    print("El valor del error es de.", valorError)

metodoSecante()

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
plt.title('Secante')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()
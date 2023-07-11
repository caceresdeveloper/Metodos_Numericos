import numpy as np
import matplotlib.pyplot as plt
import math as m

#variables
#funciones
def funcion(x):
    try:
        funcionB = (np.exp(x) / 2) + ((1/3) * x**2) - (1/x**3) - 2
        return funcionB
    except ZeroDivisionError:
        return np.inf
    
def funcionPuntoMedio(valorxi,valorxu):
    xr = (valorxi+valorxu)/2
    return xr

def error(valor1,valor2):
    resultado = abs(((valor1-valor2)/valor1)*100)
    return resultado
#entradas

#procedimiento

def metodoBiseccion():
    global raiz,puntos
    puntos = []
    raiz = 0
    contador = 0
    xi = 1
    xu = 2
    while True:
        xr = funcionPuntoMedio(xi,xu)
        fxi = round(funcion(xi), 5)
        fxr = round(funcion(xr), 5)
        valorError = error(xu,xi)
        print("i ", contador + 1, " xr=", xr, " xi=",xi, " xu=",xu, " fxi=",fxi," fxr=",fxr)
        if fxi*fxr < 0:
            xu=xr
        elif fxi*fxr > 0:
            xi=xr 
        contador += 1
        raiz = xu
        puntos.append(raiz)

        if valorError <= 0.01:
            print("El resultado de fx se acerca a cero. converge  acerca a la raiz.")
            break
    print("el valor del error es de.",valorError)


metodoBiseccion()
#salidas

#Graficas 
x = np.linspace(-2, 2, 100)
y = funcion(x)

plt.plot(x, y, 'b')
plt.axhline(y=0,color='black',linestyle='--')
plt.axvline(x=0,color='black',linestyle='--')
plt.scatter(raiz,0,color='red')
for i in range(len(puntos)):
    plt.scatter(puntos[i],0,color='green',s=10)
plt.ylim(-2, 2)  # Ajustar el límite del eje y
plt.title('Biseccion')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()
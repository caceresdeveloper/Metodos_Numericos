import numpy as np
import matplotlib.pyplot as plt
import math as m

#variables 
x0 = None
#Funciones
def funciong2(x):
    transf2 = 2*x**2 - 5
    return transf2

def funcionN(valor):
    funcion = 2*valor**2 - valor - 5
    return funcion 

def funciong1(x):
    resultado = np.sqrt((x+5)/2)
    return resultado

def error(valor1,valor2):
    resultado = abs((valor1-valor2)/valor1)
    return resultado

#Entradas
for i in range(-10, 11):
    transf2 = funciong2(i)
    if x0 is None or abs(transf2) < abs(x0):
        x0 = transf2
print("El número más cercano a cero es:", x0)

#Procedimiento
#Entradas
contador = 0
xi = x0
umbral = 1000  # Umbral de divergencia
while contador < 10:
    gx = round(funciong2(xi),2)
    fx = round(funcionN(xi),5)
    print("i", contador+1 ," ","xi"," ",xi,"gx"," ", gx , "fx"," ",fx)
    if abs(gx) > umbral:
        print("El resultado de gx se aleja de cero. La solución ha divergido 2*x**2 - 5 no es la solucion.")
        break
    xi = gx 
    contador += 1
#Salidas
contador1 = 0
xi1 = x0
raiz = 0
puntos = []
while True:
    gx1 = round(funciong1(xi1), 5)
    fx1 = round(funcionN(xi1), 5)
    valorError = error(gx1, xi1)
    print("i", contador1 + 1, "xi", xi1, "gx", gx1, "fx", fx1)
    xi1 = gx1
    contador1 += 1
    raiz = gx1
    puntos.append(raiz)

    if valorError <= 0.001:
        print("El resultado de fx se acerca a cero. converge,2*x**2 -x - 5 se acerca a la raiz.")
        break

print("el valor del error es de.",valorError)

#Graficas 
x = np.linspace(-3, 3, 50)
y1 = funcionN(x)
y2 = funciong1(x)

# Gráfica de funcionN(x)
plt.subplot(2, 1, 1)  # 2 filas, 1 columna, primera figura
plt.plot(x, y1, 'b')
plt.axhline(y=0,color='black',linestyle='--')
plt.axvline(x=0,color='black',linestyle='--')
plt.scatter(raiz,0,color='red')
plt.title('Raiz(x)')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las y')

# Gráfica de funciong1(x)
plt.subplot(2, 1, 2)  # 2 filas, 1 columna, segunda figura
plt.plot(x, y1, 'b')
plt.axhline(y=0,color='black',linestyle='--')
plt.axvline(x=0,color='black',linestyle='--')
for i in range(len(puntos)):
    plt.scatter(puntos[i],0,color='red')
plt.title('Funcion N(x)')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las y')

plt.tight_layout()  # Ajusta los subplots para evitar superposiciones
plt.show()
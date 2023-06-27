import numpy as np
import matplotlib.pyplot as plt
# Función que permite calcular el cuadrado de un valor dado como parámetro
def cuadrado(valor):
    respuesta = valor ** 2
    return respuesta

# ENTRADAS
print("Digite el valor a elevar al cuadrado")
valor=int(input())
# PROCEDIMIENTO
respuesta=cuadrado(valor)
# SALIDAS
print("Hola")
print(f"{valor} elevado al cuadrado es = {respuesta}")
# GRÁFICAS
x = np.linspace(-5,5,11)
y=cuadrado(x)
plt.plot(x,y,'r')
plt.title('Cuadrado de un valor')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las y')
plt.show()#Permite mostrar la gráfica de lo definido en la función plot
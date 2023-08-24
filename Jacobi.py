import numpy as np

def ec1(y):
    return (y/4 + 1/4)

def ec2(x, z):
    return (x/4 + z/4 + 1/4)

def ec3(y, w):
    return (y/4 + w/4 + 1/4)

def ec4(z):
    return (z/4 + 1/4)

# Valor inicial para las incógnitas
xV = 0
yV = 0
zV = 0
wV = 0

# Número máximo de iteraciones
max_iterations = 10

# Tolerancia para la convergencia
tolerance = 0.0002150488004982819

# Iteración inicial
iteration = 0

while iteration < max_iterations:
    x_new = ec2(yV, zV)
    y_new = ec1(xV)
    z_new = ec4(wV)
    w_new = ec3(yV, wV)
    
    distance = np.linalg.norm(np.array([x_new, y_new, z_new, w_new]) - np.array([xV, yV, zV, wV]))
    
    print(f"Iteration {iteration + 1}:")
    print("x:", x_new)
    print("y:", y_new)
    print("z:", z_new)
    print("w:", w_new)
    print("Error:", distance)
    print("------------------------")
    
    if distance <= tolerance:
        print(f"Converged after {iteration + 1} iterations")
        break
    
    xV, yV, zV, wV = x_new, y_new, z_new, w_new
    iteration += 1
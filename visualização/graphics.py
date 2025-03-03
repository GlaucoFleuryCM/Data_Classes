import matplotlib.pyplot as mpl
import numpy as np

def Function(theta, x):
    y = (theta[1] / theta[2]) * x
    y += theta[0] / theta[2]

    return -y

def Gráfico(points, theta):
    fig, ax = mpl.subplots()

    ax.set_xlim(0,10)
    ax.set_ylim(0,10)

    ax.scatter(points[0][:30], points[1][:30], color = 'red', label = 'Grupo Vermelho')
    ax.scatter(points[0][30:], points[1][30:], color = 'blue', label = 'Grupo Azul')

    X = np.linspace(0, 10, 100)
    Y = Function (theta, X)

    ax.plot(X, Y, label = 'Perceptron', color = 'black')

    mpl.show()    


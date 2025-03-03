import numpy as np
import pdb 

#vê se classificamos o ponto errado ou certo
def Belongs(theta, position, label):
    aux = np.dot(theta, position)
    aux = aux * label

    return aux

#algoritmo do modelo;
#data = matriz com coluna 0 = X, 1 = Y,  2 = tmp;
#data_size = 60 pontos;
def Perceptron(T, theta, lr, data):
    for t in range(T):
        y = +1
        for i in range(60):
            if (i >= 30):
                y = -1

            if (Belongs(theta,data[:,i],y) <= 0):
                theta = theta + y * lr * data[:,i]

    return theta
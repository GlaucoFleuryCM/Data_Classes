import numpy as np
import random

def Gen_Data():
    #randomiza os centros dos dados em x;
    mean_X = np.random.uniform(0,10,2)

    #gerando os dados (30 casos pra cada);
    #Data_Set 1 será negativo (y = -1)
    #Data_Set 2, positivo (y = +1)
    X1 = np.random.normal(mean_X[0], 0.8, 30)
    Y1 = np.random.normal(8, 0.8, 30)

    X2 = np.random.normal(mean_X[1], 0.8, 30)
    Y2 = np.random.normal(2, 0.8, 30)

    #formando as matrizes:
    X = np.append(X1, X2)
    Y = np.append(Y1, Y2)
    aux = np.full(60,1)
    Data = np.array([X, Y, aux])
    
    return Data

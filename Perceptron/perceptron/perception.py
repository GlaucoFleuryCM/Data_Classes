import numpy as np
import pdb 

#vê se classificamos o ponto errado ou certo
def Belongs(theta, position, label):
    aux = np.dot(theta, position)
    aux = aux * label

    return aux

#algoritmo do modelo;
#wall = ponto que separa os grupos
#size = quantos exemplos tomar no data_set
#lr = learning rate
def Perceptron(T, theta, lr, data, size, wall):
    pdb.set_trace()

    #gambiarra pro caso 3D;
    if (size == 100):
        data = data.to_numpy().T
        #adicionando a parte do bias;
        aux = np.full(150,1)
        data = np.vstack((data, aux))

    for t in range(T):
        flag = 0
        for i in range(size):
            #diferencia as classes;
            if (i >= wall):
                y = -1
            else:
                y = 1    

            if (Belongs(theta,data[:,i],y) <= 0):
                theta = theta + y * lr * data[:,i]
                flag = 1
                print (f'pesos fodas = {theta}')

        if (flag == 0):
            print (f'fim do treino no ciclo {t}')
            break

    return theta
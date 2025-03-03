import numpy as np
from data.generator import Gen_Data
from perceptron.perception import Perceptron
from visualização.graphics import Gráfico

#lendo os hiperparâmetros pro perceptron;
learning_rate = float(input("Qual o learning rate desejado? "))
iterations = int(input("Quantas iterações sobre o dataset você deseja? "))
theta2, theta1, theta0 = map(float, input("Valores para \u03B82, \u03B81 e \u03B80, respectivamente: ").split())
theta = (theta2, theta1, theta0)

#trazendo o data_set pro treinamento;
Data = Gen_Data()

Gráfico(Data, theta)

#inicializando theta e treinando o perceptron;
theta = np.asanyarray(theta)
theta = Perceptron(iterations, theta, learning_rate, Data)

#mostrando no gráfico o resultado;
Gráfico(Data, theta)
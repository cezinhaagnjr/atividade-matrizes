import numpy as np

matriz = np.array([[2, 5, 7],
                   [1, -3, 4],
                   [3, 2, -6]])

determinante = np.linalg.det(matriz)
print(determinante)

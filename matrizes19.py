import numpy as np

matriz = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

soma_colunas = np.sum(matriz, axis=0)
print(soma_colunas)

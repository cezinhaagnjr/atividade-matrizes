import numpy as np


matriz_np = np.array([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])

print("Matriz Numpy:\n", matriz_np)

print("Soma dos elementos da matriz:", np.sum(matriz_np))
print("Média dos valores da matriz:", np.mean(matriz_np))
print("Transporta da matriz: \n", matriz_np.T)
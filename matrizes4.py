import numpy as np
my_array = np.array([0, 1 , 2 , 3 , 4])

my_list = [ 0 , 1 , 2 , 3 , 4]

matriz_1 = np.array([my_list, my_list, my_list])
print(matriz_1)
print("-------------")

matriz_2 = np.array([my_array,my_array, my_array])
print(matriz_2)
print("-----------")
matriz_2 += 3
print(matriz_2)
print("-----------")
matriz_2 -= 1
print(matriz_2)
print("-----------")

matriz_2 *= 3
print(matriz_2)
print("-----------")

matriz_2 = matriz_2/2
print(matriz_2)

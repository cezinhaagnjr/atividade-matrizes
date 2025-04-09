matriz = [[1, 20, 3], [4, 15, 6], [7, 8, 9]]
todos = [num for linha in matriz for num in linha]
print("Maior:", max(todos))
print("Menor:", min(todos))

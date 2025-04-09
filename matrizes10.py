matriz = [[i + j for j in range(4)] for i in range(4)]
numero = 5
existe = any(numero in linha for linha in matriz)
print("Existe?", existe)

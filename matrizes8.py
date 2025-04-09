matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = sum(sum(linha) for linha in matriz)
media = soma / 9
print(media)

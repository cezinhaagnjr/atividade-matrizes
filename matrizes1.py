matriz =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print("Elemento na posição (2,3):",matriz[1][2])

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
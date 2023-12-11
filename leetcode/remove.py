

matrix = [1, 5, 2, 6, 2, 5, 2, 5, 1]


def eliminar():
  
  sorted(matrix, reverse= True)

  if 2 in matrix:
    print(matrix.remove(2))

print(matrix)
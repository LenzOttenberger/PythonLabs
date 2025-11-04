rows = int(input('Введите кол-во строк матрицы: '))
cols = int(input('Введите кол-во столбцов матрицы: '))
matrix = []

for i in range(rows):
    row = str(
        input(f'Введите строку номер {i + 1}: '))
    row = row.split()
    row = [int(item) for item in row]
    matrix.append(row)


def transpose_matrix(matrix):
    transposed = [[row[i] for row in matrix] for i in range(cols)]
    return transposed


def print_matrix(matrix):
    print('Вывожу матрицу: ')
    for row in matrix:
        print(row)


print_matrix(matrix)
transposed = transpose_matrix(matrix)
print_matrix(transposed)

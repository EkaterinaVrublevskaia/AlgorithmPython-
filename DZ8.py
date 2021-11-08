"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

"""

matrix = []

for i in range(4):
    matrix.append([])
    s = 0
    for j in range(4):
        user_n = int(input(f'Введите элемент {i+1} и {j+1} столбца: '))
        s += user_n
        matrix[i].append(user_n)

    matrix[i].append(s)

for k in matrix:
    print(('{:>4d}' * 5).format(*k))
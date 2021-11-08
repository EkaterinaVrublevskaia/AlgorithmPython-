"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random
a = [random.randint(1, 99) for k in range(15)]
print(f'Случайный массив для изменения: {a}')

index_min = 0
index_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_max]:
        index_max = i
    if a[i] < a[index_min]:
        index_min = i
a[index_min], a[index_max] = a[index_max], a[index_min]

print(' '.join([str(i) for i in a]))

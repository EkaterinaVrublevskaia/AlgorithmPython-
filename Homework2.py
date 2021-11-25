"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(li):
    if len(li) <= 1:
        return li

    middle = len(li) // 2
    left = merge_sort(li[:middle])
    right = merge_sort(li[middle:])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i == len(left):
        res.extend(right[j:])
    else:
        res.extend(left[i:])

    return res

n = int(input("Введите количество значений случайного массива: "))
a = [random.uniform(0, 50) for _ in range(n)]
print(a)
print(merge_sort(a))




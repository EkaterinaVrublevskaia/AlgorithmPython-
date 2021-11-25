"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random
import math


def my_median(array):
    n = len(array)
    i = n // 2
    if n % 2:
        return sorted(array)[i]

    return sum(sorted(array)[i - 1:i + 1]) / 2


"""
def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2** k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array
"""
m = int(input("Введите натуральное число для расчета размера случайного массива: "))
a = [random.randint(0, 50) for _ in range((2 * m) + 1)]

print(f'Массив: {a}')
# print(shellSort(a))
print(f'Медиана: {my_median(a)}')

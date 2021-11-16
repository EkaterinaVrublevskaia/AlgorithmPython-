"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

"""
# пракическое задание 3.3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import timeit
import cProfile


# 1
def min_max(a):
    index_min = 0
    index_max = 0
    for i in range(1, len(a)):
        if a[i] > a[index_max]:
            index_max = i
        if a[i] < a[index_min]:
            index_min = i
    a[index_min], a[index_max] = a[index_max], a[index_min]
    return ' '.join([str(i) for i in a])


a = [random.randint(1, 99) for k in range(15)]

print(a)
print(min_max(a))

i = 0
while True:
    if i <= 10:
        i += 1
        print(timeit.timeit('min_max(a)', number=1000, globals=globals()))
        # cProfile.run('min_max(a)') #7 function calls in 0.000 seconds

# 0.005148400000000004
# 0.005111699999999997
# 0.008615900000000003
# 0.0046683
# 0.0040525000000000005
# 0.004531199999999999
# 0.004032099999999997
# 0.004340399999999994
# 0.005404300000000001
# 0.0038122000000000017
# 0.0038163999999999976

# cProfile.run('min_max(a)') #7 function calls in 0.000 seconds
# Опимальный по скорости. О(n)


# 2 замена по индексу, убираем array.index - замена чиселв результате. C использованием min and max.
list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [random.randint(1, 99) for _ in range(15)]


def min_max(array):
    i_min = array.index(min(array))
    # i_min = min(array)
    i_max = array.index(max(array))
    # i_max = max(array)
    if i_min > i_max:
        return i_min, i_max
    return i_max, i_min


print(min_max(list_a))
print(min_max(a))

i = 0
while True:
    if i <= 10:
        i += 1
        print(timeit.timeit('min_max(a)', number=1000, globals=globals()))
        # cProfile.run('min_max(a)') # 8 function calls in 0.000 seconds
# 0.0012082999999999955
# 0.0008845999999999993
# 0.0010447000000000026
# 0.000805199999999999
# 0.0008279999999999954
# 0.0008893999999999985
# 0.0009025000000000005
# 0.0008873999999999965
# 0.000931299999999996
# 0.0010979999999999948
# 0.0010143999999999986
# 8 function calls in 0.000 seconds
# Оптимальный по скорости. О(n)

# 3

# def min_max(n):
#    max_v = max(n)
#    min_v = min(n)
#    i_min = [i for i, j in enumerate(n) if j == min_v]
#    i_max = [i for i, j in enumerate(n) if j == max_v]
#    for k in i_min:
#        n[k] = max_v
#    for k in i_max:
#        n[k] = min_v
#    return n

# n = [random.randint(1, 99) for _ in range(15)]
# print(n)
# print(min_max(n))


i = 0
while True:
    if i <= 10:
        i += 1
        print(timeit.timeit('min_max(n)', number=1000, globals=globals()))
        # cProfile.run('min_max(n)') #8 function calls in 0.000 seconds


# 0.003136800000000002
# 0.002887899999999999
# 0.004077299999999999
# 0.0054751999999999995
# 0.002836100000000001
# 0.0028839000000000017
# 0.0030033999999999964
# 0.002534700000000001
# 0.0031513999999999986
# 0.0025411000000000045
# 0.0025549000000000127

# Более меденный в обрабоки, так как используеся enumerate(n)
def min_max(a):
    i = [{min(a): max(a), max(a): min(a)}.get(x, x) for x in a]
    return i


a = [random.randint(1, 99) for _ in range(15)]
# print(a)
i = 0
while True:
    if i <= 10:
        i += 1
        print(timeit.timeit('min_max(a)', number=1000, globals=globals()))
        cProfile.run('min_max(a)')  # 80 function calls in 0.000 seconds

# 0.024405699999999995
# 0.019656900000000005
# 0.018201300000000004
# 0.018523200000000004
# 0.01863759999999999
# 0.018492199999999986
# 0.0177157
# 0.019672899999999993
# 0.01941000000000001
# 0.021201700000000018
# 0.022267100000000012
# Самый Медленный.

"""
Вывод. 
По скорости 1 и 2 варианты показывают лучшие результаты. 2 лучше 1. Принцип в них один, но 2 оптимальнее, в ввиду
того что используется метод array и функции min, max + сама функция проще. 
О(n)

= Можно было бы выбрать другой пример. Разбирала 3.8 - марицы еще. 

"""

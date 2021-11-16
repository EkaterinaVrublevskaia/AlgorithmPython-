"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
"""
import math
import timeit
import cProfile

'''Функция поиска i-го простого числа,
 без использования алгоритма «Решето Эратосфена»
 '''


def prime(i):
    if (math.factorial(i - 1) + 1) % i != 0:
        return "Это составное число"
    else:
        return "Это простое число"


print(prime(101))

# print(timeit.timeit('prime(10)', number=1000, globals=globals())) #0.00030939999999999787
# print(timeit.timeit('prime(50)', number=1000, globals=globals())) #0.0017928000000000041
# print(timeit.timeit('prime(100)', number=1000, globals=globals())) #0.0019360999999999996
# print(timeit.timeit('prime(199)', number=1000, globals=globals())) #0.004455799999999996
# print(timeit.timeit('prime(300)', number=1000, globals=globals())) #0.008416100000000003
# print(timeit.timeit('prime(500)', number=1000, globals=globals())) #0.021556
# print(timeit.timeit('prime(600)', number=1000, globals=globals())) #0.031078800000000004


# cProfile.run('prime(10)') # 5 function calls in 0.000 seconds
# cProfile.run('prime(100)') # 5 function calls in 0.000 seconds
# cProfile.run('prime(300)') # 5 function calls in 0.000 seconds
# cProfile.run('prime(500)') # 5 function calls in 0.000 seconds
# cProfile.run('prime(700)') # 5 function calls in 0.000 seconds
# cProfile.run('prime(999)') # 5 function calls in 0.000 seconds
# cProfile.run('prime(2000)') # 5 function calls in 0.000 seconds
"""
Вывод:
O(n). 
cProfile.run дае 0.000 скорее всего что-то делаю не так.
"""


# Вариант поиска простого числа:
def prime(i):
    n = 2
    j = 0
    while n ** 2 <= i and j != 1:
        if i % n == 0:
            j = 1
        n += 1
    if j == 1:
        return "Это составное число"
    else:
        return "Это простое число"


print(prime(102))

# print(timeit.timeit('prime(10)', number=1000, globals=globals())) #0.0008413999999999991
# print(timeit.timeit('prime(50)', number=1000, globals=globals())) # 0.0007060000000000018
# print(timeit.timeit('prime(100)', number=1000, globals=globals())) # 0.0007155000000000009
# print(timeit.timeit('prime(199)', number=1000, globals=globals())) #0.0046301999999999975
# print(timeit.timeit('prime(300)', number=1000, globals=globals())) # 0.0007965000000000021
# print(timeit.timeit('prime(500)', number=1000, globals=globals())) # 0.0006557000000000021
# print(timeit.timeit('prime(600)', number=1000, globals=globals())) # 0.0006228999999999991

# cProfile.run('prime(10)') # 4 function calls in 0.000 seconds
# cProfile.run('prime(100)')
# cProfile.run('prime(300)')
# cProfile.run('prime(500)') # 4 function calls in 0.000 seconds
# cProfile.run('prime(700)')
# cProfile.run('prime(999)')
# cProfile.run('prime(1010)')  # 4 function calls in 0.000 seconds
"""
Вывод: 


"""

'''Функция поиска i-го простого числа,
используя алгоритм «Решето Эратосфена»
'''


def sieve(i):
    a = []
    for n in range(i + 1):
        a.append(n)
    a[1] = 0
    n = 2
    while n <= i:
        if a[n] != 0:
            j = n + n
            while j <= i:
                a[j] = 0
                j = j + n
        n += 1
    a = set(a)
    a.remove(0)
    return a


# print(sieve(500))

# print(timeit.timeit('sieve(10)', number=1000, globals=globals())) #0.003030100000000001 , 0.0026604999999999997
# print(timeit.timeit('sieve(50)', number=1000, globals=globals())) # 0.014203099999999996 , 0.010927800000000001
# print(timeit.timeit('sieve(100)', number=1000, globals=globals())) # 0.0582536 ,  0.0363836
# print(timeit.timeit('sieve(199)', number=1000, globals=globals())) # 0.08062620000000001 , 0.0882877
# print(timeit.timeit('sieve(300)', number=1000, globals=globals())) # 0.0920193 , 0.10995590000000001
# print(timeit.timeit('sieve(500)', number=1000, globals=globals())) # 0.13961900000000002 , 0.1579784
# print(timeit.timeit('sieve(600)', number=1000, globals=globals())) # 0.2346783 , 0.1848707


# cProfile.run('sieve(10)') # 0.000 and append - 11 ncalls
# cProfile.run('sieve(100)') # 0.000 and append - 101 ncalls
# cProfile.run('sieve(300)') # 0.000 and append - 301 ncalls  , 306 function calls in 0.000 seconds
# cProfile.run('sieve(500)') # 0.000 and append - 501 ncalls
# cProfile.run('sieve(700)') # 0.000 and append - 701 ncalls
# cProfile.run('sieve(999)') # 0.001 and append - 1000 ncalls
# cProfile.run('sieve(1010)') # 0.001 and append - 1011 ncalls ,  1016 function calls in 0.001 seconds

"""
Вывод: 
В первом примере вывод не о какое последует, а результат того числа, чо ввели. 
При исопльзовании функции факориала, обрабока возрасает при увелечении запрашиваемого числа, или не меняется если
использовать циклы. O(n)
Во втором примере (решето) cкорось возрасает где-то 1 к 10. О(n)
При проверки cProfile.run выдает 0.000, но обработка запроса сама в себе зависит от числа, которое вводит пользователь или мы.

= Сделала не то, не отимизировала ворой код. 
"""

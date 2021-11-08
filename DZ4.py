"""
Определить, какое число в массиве встречается чаще всего.
"""
import random
a = [random.randint(0, 99) for k in range(20)]
print(f'Случайный массив для изменения: {a}')

a_set = set(a)
z = None
max_number = 0
for i in a_set:
    j = a.count(i)
    if j > max_number:
        max_number = j
        z = i

print(f'Число {z}, встречается {max_number} раза')
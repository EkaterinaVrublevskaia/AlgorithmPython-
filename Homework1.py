"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections

company = collections.namedtuple('company', ['name', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'profit'])
company_ = []
quantity = int(input("Введити какое количество компаний вы будете заполнять данными: "))
count = 0
for i in range(quantity):
    name = input(f"Название {i + 1}-ого предприятия: ")
    quarter_1 = int(input("Прибыль за 1 квартал: "))
    quarter_2 = int(input("Прибыль за 2 квартал: "))
    quarter_3 = int(input("Прибыль за 3 квартал: "))
    quarter_4 = int(input("Прибыль за 4 квартал: "))
    profit = quarter_1 + quarter_2 + quarter_3 + quarter_4
    count += profit
    company_.append(
        company(name=name, quarter_1=quarter_1, quarter_2=quarter_2, quarter_3=quarter_3, quarter_4=quarter_4,
                profit=profit))
    print(f'Предприятие: {name} прибыль за год - {profit}')
    count += profit

avg_val = count / quantity
for company in company_:
    if company.profit >= avg_val:
        print(f"Предприятия с прибылью выше средней {avg_val}: {company.name}")
for company in company_:
    if company.profit < avg_val:
        print(f"Предприятия с прибылью неже средней {avg_val}: {company.name}")

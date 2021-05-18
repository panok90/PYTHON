"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import defaultdict
def_dict = defaultdict(list)
n = int(input('Введите количество предприятий: '))
profit_sum = 0
for i in range(1, n+1):
    company = input(f'№{i} Наименование: ')
    profit_quarter = profit_yar = 0
    for j in range(1, 5):
        profit_quarter = float(input(f'{company}.  Прибыль за {j} квартал: '))
        def_dict[company].append(profit_quarter)  # В списке будем хранить прибыль по квартально
        profit_yar += profit_quarter
    profit_sum += profit_yar
    def_dict[company].append(profit_yar)  # В конце списка записываем годовую прибыль


average_profit = round(profit_sum / n, 2)
print(f'Средняя прибыль (за год для всех предприятий): {average_profit}')
str_max = str_min = ""
for company in def_dict:
    if def_dict[company][-1] > average_profit:
        str_max += f'{company} - {def_dict[company][-1]}   '
    else:
        str_min += f'{company} - {def_dict[company][-1]}   '

print(f'Прибыль выше среднего: {str_max}')
print(f'Прибыль ниже среднего: {str_min}')

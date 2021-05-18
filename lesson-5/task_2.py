"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
[‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def func_sum_hex(hex_num, x, y):

    result_list = deque()
    k = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            result = hex_num.index(x.pop()) + hex_num.index(y.pop()) + k
        else:
            result = hex_num.index(x.pop()) + k
        if result < 16:
            result_list.appendleft(hex_num[result])
            k = 0
        else:
            result_list.appendleft(hex_num[result - 16])
            k = 1
    if k:
        result_list.appendleft('1')
    return list(result_list)


def func_prod_hex(hex_num, x, y):
    result_list = deque()
    view = deque([deque() for _ in range(len(y))])  # Временный массив
    x, y = deque(x), deque(y)
    k = 0

    for i in range(len(y)):
        index = hex_num.index(y.pop())
        for j in range(len(x) - 1, -1, -1):
            view[i].appendleft(index * hex_num.index(x[j]))
        for _ in range(i):
            view[i].append(0)
    for _ in range(len(view[-1])):
        result = k
        for i in range(len(view)):
            if view[i]:
                result += view[i].pop()
        if result < 16:
            result_list.appendleft(hex_num[result])
        else:
            result_list.appendleft(hex_num[result % 16])
            k = result // 16
    if k:
        result_list.appendleft(hex_num[k])

    return list(result_list)


a = input('Введите 1-е шестнадцатиричное число: ').upper()
b = input('Введите 2-е шестнадцатиричное число: ').upper()
print(a, b)
HEX = [str(i) for i in range(10)]
HEX.extend(['A', 'B', 'C', 'D', 'E', 'F'])
print(f'{a} + {b} = {"".join(func_sum_hex(HEX, a, b))}')

print(f'{a} * {b} = {"".join(func_prod_hex(HEX, a, b))}')

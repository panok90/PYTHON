"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
"""
2. Во втором массиве сохранить индексы четных элементов первого массива. Например,
если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import sys
from random import randint


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)

# 1-й ВАРИАНТ. Резултат будем выводить в списке


def func_list(list_):
    even = list()
    for item in range(len(list_)-1):
        if arr[item] % 2 == 0:
            even.append(item)
    print(f'##########################################-LIST-############################################')
    print(f'Массив: {list_}, индексы четных: {even}')
    show(even)

# 2-й ВАРИАНТ. Резултат будем выводить в множестве, т.к. индексы уникальны.


def func_set(list_):
    even = set()
    for item in range(len(list_)-1):
        if arr[item] % 2 == 0:
            even.add(item)
    print(f'##########################################-SET-############################################')
    print(f'Массив: {list_}, индексы четных: {even}')
    show(even)

# 3-й ВАРИАНТ. Резултат будем выводить в dict.


def func_dict(list_):
    even = dict()
    i = 1
    for item in range(len(list_)-1):
        if arr[item] % 2 == 0:
            even[i] = item
            i += 1
    print(f'##########################################-DICT-############################################')
    print(f'Массив: {list_}, индексы четных: {even}')
    show(even)


N = int(input(f'Введите количество элементов массива: '))
arr = list()
for i in range(N):
    arr.append(randint(0, 100))
func_list(arr)
func_set(arr)
func_dict(arr)

"""
ОС WINDOWS 10 x64 (16Gb - ОЗУ), pycharm x64

Введите количество элементов массива: 10
##########################################-LIST-############################################
Массив: [17, 13, 40, 50, 46, 25, 18, 5, 59, 43], индексы четных: [2, 3, 4, 6]
type(obj)=<class 'list'>, sys.getsizeof(obj)=88, obj=[2, 3, 4, 6]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=6

Список, из трех вариантов самый маленький по объему, т.к. он хранится непрерывно в памяти. Кроме ссылок 
на сами объекты компилятор выделяет небольшой резер (без резерва объем был бы еще меньше).
##########################################-SET-############################################
Массив: [17, 13, 40, 50, 46, 25, 18, 5, 59, 43], индексы четных: {2, 3, 4, 6}
type(obj)=<class 'set'>, sys.getsizeof(obj)=216, obj={2, 3, 4, 6}
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=6

Множество,большая по объему коллекция. за счет хронимого хэша(уникального ключа)
##########################################-DICT-############################################
Массив: [17, 13, 40, 50, 46, 25, 18, 5, 59, 43], индексы четных: {1: 2, 2: 3, 3: 4, 4: 6}
type(obj)=<class 'dict'>, sys.getsizeof(obj)=232, obj={1: 2, 2: 3, 3: 4, 4: 6}
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=1
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=6

Словарь, самоя большая коллекция среди наших вариантов.
"""
"""
Вывод:
Наш результат наглядно показывает, что для поставленных задач, очень важно правильно определять объекты для хранения
данных. По полученным результатам видно, что одни и теже данные могут занимать в разы больше объем памяти, а в 
больших задачах такое расточительство может привести к ее не хватке.
"""


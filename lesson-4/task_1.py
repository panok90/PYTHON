"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
практического задания первых трех уроков.
"""
"""
2 урок 
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
 то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
import cProfile
import timeit
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

""" ВАРИАНТ 1 """


def func_rec(number, a=0, b=0):
    if number == 0:
        return
    if number % 2:
        func_rec(number//10, a, b+1)
    else:
        func_rec(number//10, a+1, b)


""" ВАРИАНТ 2 """


def func_str(number):
    list_ = str(number)
    even = uneven = 0
    for i in list_:
        if int(i) % 2:
            uneven += 1
        else:
            even += 1


""" ВАРИАНТ 3 """


def func_int(number):
    even = uneven = 0
    while number > 0:
        if number % 2:
            uneven += 1
        else:
            even += 1
        number = number // 10


arg = 4563654354253264346235243
a = timeit.timeit("func_rec(arg)", number=1_000_000, globals=globals())
print(a)  # 4.2298576
b = timeit.timeit("func_str(arg)", number=1_000_000, globals=globals())
print(b)  # 2.9747284
c = timeit.timeit("func_int(arg)", number=1_000_000, globals=globals())
print(c)  # 2.6199523000000005


arg1 = 4563654354253264346353251145423235463464352451512
cProfile.run('func_rec(arg1)')
"""
         53 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     50/1    0.000    0.000    0.000    0.000 task_1.py:17(func_rec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('func_str(arg1)')
"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:29(func_str)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('func_int(arg1)')

"""
 4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:42(func_int)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


names = ('func_rec', 'func_str', 'func_int')
y_pos = np.arange(len(names))
time = [a, b, c]
plt.bar(y_pos, time, align='center', alpha=0.5)
plt.xticks(y_pos, names)
plt.ylabel('time')
plt.title('function')
plt.show()


"""
1. При подсчете времени исполнения кода модулем timeit видно, что медленнее всего в поставленной задаче работала
    рекурсия, а циклы примерно показали одинаковое время.
2. Модуль cProfile при подсчете времени выполнения незначительных задач при округлении выдает 0. И понять, на
    сколько какой вариант отличается от остальных не возможно. Единственное хорошо видно, что рекурсия вызывалась очень
    большое количество раз.
"""

"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
 то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def func_rec(number, a=0, b=0):
    if number == 0:
        print(f'Четных: {a}, нечетных: {b}')
        return
    d = number % 10
    if d % 2:
        func_rec(number//10, a, b+1)
    else:
        func_rec(number//10, a+1, b)


arg = int(input('Введите целое число: '))
func_rec(arg)

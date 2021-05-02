"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""


def func_rec(n, sum_elem=0, num=1):
    if n == 0:
        print(f'{sum_elem}')
        return
    sum_elem += num
    num /= -2
    func_rec(n-1, sum_elem, num)


arg = int(input(f'Введите количество элементов: '))
func_rec(arg)

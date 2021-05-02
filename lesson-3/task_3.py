"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint


def func_rec(arr, i=0, imn=0, imx=0):
    ln = len(arr)
    i += 1
    if i == ln:
        arr_new = arr.copy()
        mn = arr[imn]
        mx = arr[imx]
        arr_new[imn] = mx
        arr_new[imx] = mn
        print(f'Исходный: {arr}, результат: {arr_new}')
        return
    if arr[imn] > arr[i]:
        func_rec(arr, i, i, imx)
    elif arr[i] > arr[imx]:
        func_rec(arr, i, imn, i)
    else:
        func_rec(arr, i, imn, imx)


n = int(input(f'Введите количество элементов массива: '))
lst = list()
while n > 0:
    lst.append(randint(0, 100))
    n += 1
func_rec(lst)

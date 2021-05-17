"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import random


def func_merge_sort(arr, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        func_merge_sort(arr, start, mid)
        func_merge_sort(arr, mid, end)
        func_merge(arr, start, mid, end)
    return arr


def func_merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            arr[k] = right[j]
            j = j + 1
            k = k + 1


array = [round(random() * 50, 2) for _ in range(10)]
print(f'Исходный: {array} --> Сортированный: {func_merge_sort(array, 0, len(array))}')
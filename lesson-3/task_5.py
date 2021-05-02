"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import random

n = 10
arr = []
for i in range(n):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < n:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[index] < arr[i] < 0:
        index = i
    i += 1

print(f'Элемент: {index + 1}, значение: {arr[index]}')

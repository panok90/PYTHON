"""
4. Определить, какое число в массиве встречается чаще всего.
"""

arr = [1, 2, 4, 44, 22, 65, 2, 44, 44, 44, 54, 1]
n = len(arr)
mx_val = 0
imx = 0
for i in range(n):
    val = arr[i]
    mx = 0
    for j in range(n):
       if arr[j] == val:
           mx += 1
    if mx > mx_val:
        mx_val = mx
        imx = val
if mx_val > 0:
    print(f'Число {imx} - {mx_val} раз(а)')
else:
    print(f'Все элементы уникальны')

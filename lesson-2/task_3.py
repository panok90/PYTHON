"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, то надо вывести число 6843.
"""


def func_reverse(number, b=0):
    if number == 0:
        print(b)
        return
    b = b * 10 + number % 10
    func_reverse(number//10, b)


arg = int(input(f"Введите целое число: "))
func_reverse(arg)

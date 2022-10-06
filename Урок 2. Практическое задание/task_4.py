"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_elem(num_row, el_row=1.0, res=0.0):
    if num_row == 0:   # Базовый случай
        return res
    res = res + el_row
    el_row = (el_row / 2) * -1
    num_row -= 1
    return sum_elem(num_row , el_row, res)


if __name__ == '__main__':
    print("Сумма элементов ряда: ",
          sum_elem(int(input('Введите количество элементов ряда: '))))

# Введите количество элементов ряда: 3
# Сумма элементов ряда:  0.75

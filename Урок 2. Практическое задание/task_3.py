"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

""" Var1, рекурсия через % и // (только для чисел) """

def revers_1(num):
    if not num // 10:   # Базовый случай
        return num
    return str(num % 10) + str(revers_1(num // 10))


if __name__ == '__main__':
    print("Обратное значение: ", revers_1(int(input('Введите число: '))))

# Введите число: 234456500
# Обратное значение:  005654432

""" Var2, рекурсия через срез """

def revers2(var):
    if len(var) == 1:
        return var
    return var[-1] + revers2(var[:-1])


print("Обратное значение: ", revers2(input("Введите данные: ")))

# Введите данные: 4567890
# Обратное значение:  0987654
#
# Введите данные: 5G2d0gf
# Обратное значение:  fg0d2G5


""" Var3 """
# А вообще, первое, что приходит на ум - простой срез,
# если конечно не надо как-то ещё изменять данные

print("Обратное значение: ", input("Введите данные для реверса: ")[::-1])

# Введите данные для реверса: 1234560
# Обратное значение:  0654321
#
# Введите данные для реверса: sdf23r  4535_,,43dsdfD
# Обратное значение:  Dfdsd34,,_5354  r32fds

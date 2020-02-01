# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


user_number_x = int(input('Введите положительное число: '))
user_number_y = int(input('Введите целое отрицательное число: '))


def my_func(x, y):
    y = abs(y)
    divider = x ** y
    result = 1 / divider
    print(result)
    return result


def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer


def my_func_1(x, y):
    y = abs(y)
    i = 0
    my_list = []
    while i != y:
        my_list.append(x)
        i += 1
    divider = multiply(my_list)
    result = 1 / divider
    print(result)


my_func(user_number_x, user_number_y)
my_func_1(user_number_x, user_number_y)



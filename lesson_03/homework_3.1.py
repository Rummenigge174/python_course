# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль..

user_number = int(input('Введите первое число: '))
user_number_1 = int(input('Введите второе число: '))


def divide_user_numbers(num1, num2):
    try:
        result = (num1 / num2)
    except ZeroDivisionError as e:
        print('Не дели на ноль')
        print('Информация об исключении', e)
        result = 0
        return result
    else:
        result = num1 / num2
        return result


print(divide_user_numbers(user_number, user_number_1))

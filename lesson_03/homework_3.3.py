# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов..

numbers = []
for i in range(1, 4):
    user_number = (input('Введите число: '))
    numbers.append(user_number)


def my_func(num1, num2, num3):
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    num3 = int(numbers[2])
    if (num1 > num2) and (num1 > num3) and (num2 > num3):
        result = num1 + num2
    elif (num1 > num2) and (num1 > num3) and (num2 < num3):
        result = num1 + num3
    elif (num1 < num2) and (num1 < num3):
        result = num2 + num3

    return result


print(my_func(numbers[0], numbers[1], numbers[2]))

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


user_number = int(input('Введите число от 0 до 100: '))

# Первый способ
my_list_1 = [7, 5, 3, 3, 2]
my_list_1.append(user_number)
my_list_1.sort(reverse=True)
print(my_list_1)

# Второй способ
my_list_2 = [7, 5, 3, 3, 2]
i = 0
my_list = my_list_2.copy()
for number in my_list_2:
    if user_number <= number:
        i += 1
my_list.insert(i, user_number)
print(my_list)
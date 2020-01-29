# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

number = int(input('Введите число от 1 до 12: '))

month_dict = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь'}
time_of_year_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима'
}

print(month_dict.get(number))
print(time_of_year_dict.get(number))

month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
time_year_list = ['зима', 'весна', 'лето', 'осень']

if number == 1:
    print(month_list[0])
    print(time_year_list[0])
elif number == 2:
    print(month_list[1])
    print(time_year_list[0])
elif number == 3:
    print(month_list[2])
    print(time_year_list[1])
elif number == 4:
    print(month_list[3])
    print(time_year_list[1])
elif number == 5:
    print(month_list[4])
    print(time_year_list[1])
elif number == 6:
    print(month_list[5])
    print(time_year_list[2])
elif number == 7:
    print(month_list[6])
    print(time_year_list[2])
elif number == 8:
    print(month_list[7])
    print(time_year_list[2])
elif number == 9:
    print(month_list[8])
    print(time_year_list[3])
elif number == 10:
    print(month_list[9])
    print(time_year_list[3])
elif number == 11:
    print(month_list[10])
    print(time_year_list[3])
elif number == 12:
    print(month_list[11])
    print(time_year_list[0])

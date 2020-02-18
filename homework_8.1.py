# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from functools import reduce

my_dict_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def sum_number(prev_el, el):
    return prev_el + el

class Date:

    def __init__(self, usr_date):
        self.usr_date = usr_date

    @classmethod
    def in_int(cls, usr_date):
        result = []
        result_1 = []
        list_date_int = []
        j = 0
        usr_list = usr_date.split('-')
        for i in usr_list:
            for el in i:
                if el in my_dict_num:
                    num = my_dict_num[el]
                    result.append(num)
                    j += 1
                    if j == 2:
                        for x in range(0, len(result)):
                            num_in_list = int(result[x]) * (10 ** (j - 1))
                            result_1.insert(x, num_in_list)
                            j -= 1
                        date_int = reduce(sum_number, result_1)
                        list_date_int.append(date_int)
                        result_1.clear()

            result.clear()
        return list_date_int

    @ staticmethod
    def valid_month(my_list):
        j = 0
        for i in my_list:
            if j == 0 and (i < 0 or i > 30):
                print('Число введено некорректно')
                break
            elif j == 1 and (i < 0 or i > 12):
                print('Месяц введен некорректно')
                break
            j += 1



        print('корректные данные')


print(Date.in_int('10-11-20'))

Date.valid_month(Date.in_int('10-13-20'))


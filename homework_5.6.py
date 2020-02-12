# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce

dict_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
my_list = []
result = []
result_1 = []
result_2 = []
final_dict = {}
i = 0
j = 0
el_in_dict = None


def sum_number(prev_el, el):
    return prev_el + el


with open('my_file_6.txt', 'r') as f_obj:
    for line in f_obj:
        my_list = line.split()
        key = my_list[0]
        print(my_list)
        for num_str in my_list:
            for el in num_str:
                if el in dict_number:
                    el_in_dict = dict_number[el]
                    result.append(el_in_dict)
                    i += 1

                else:
                    for z in range(0, len(result)):
                        if i != 0:
                            num_in_list = int(result[z]) * (10 ** (i-1))
                            result_1.insert(z, num_in_list)
                            value = reduce(sum_number, result_1)
                            i -= 1
                        else:
                            result.clear()
                            break
        result_1.clear()
        final_dict[key] = value
        key = 0
        value = 0
        print(final_dict)

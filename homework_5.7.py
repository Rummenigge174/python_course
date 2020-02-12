# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
from functools import reduce
import json
my_list = []
my_dict = {}
average = []
average_profit_dict = {}
final_list = []


def sum_number(prev_el, el):
    return prev_el + el


with open('my_file_7.txt','w') as f_obj:
    f_obj.writelines('firm_1 OOO 10000 5000\n')
    f_obj.writelines('firm_2 OOO 12000 9000\n')
    f_obj.writelines('firm_3 OOO 7000 9000\n')

with open('my_file_7.txt', 'r') as f_obj:
    for line in f_obj:
        my_list = line.split()
        revue = int(my_list[2])
        costs = int(my_list[3])
        if revue - costs > 0:
            profit = revue - costs
            key = my_list[0]
            my_dict[key] = profit
            average.append(profit)
        else:
            lose = revue - costs
            key = my_list[0]
            my_dict[key] = lose
            average.append(lose)
    sum_profit = reduce(sum_number, average)
    print(sum_profit)
    average_profit = sum_profit / len(average)
    average_profit_dict['average_profit'] = average_profit
    final_list.append(my_dict)
    final_list.append(average_profit_dict)
    print(final_list)
with open('my_file_7_1.json', 'w') as write_f:
    json.dump(final_list, write_f)
    print(final_list)





from functools import reduce

my_list = []
my_list_1 = []
def sum_number(prev_el, el):
    return prev_el + el

with open('my_file_5.txt', 'w') as f_obj:
    f_obj.writelines('123 456 789\n')
    f_obj.writelines('123\n')

with open('my_file_5.txt', 'r') as f_obj:
    for line in f_obj:
        my_list = line.split()
        for num_str in my_list:
            num_int = int(my_list[my_list.index(num_str)])
            my_list_1.append(num_int)

print(reduce(sum_number, my_list_1))

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
my_list = []
result = []
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('my_file_2.txt', 'r') as f_obj:
    for line in f_obj:
        result = line.split()
        key = result[0]
        argument = my_dict[key]
        result.pop(0)
        result.insert(0, argument)
        my_line = ' '.join(result)
        my_list.append(my_line)
    with open('my_file_2_2.txt', 'w') as f_obj_1:
        for line in my_list:
            f_obj_1.write(f'{line}\n')

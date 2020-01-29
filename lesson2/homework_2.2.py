# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
y = int(input('Введите кол-во элементов в списке: '))
for i in range(0, y):
    number = input('Введите любые данные: ')
    my_list.append(number)

result = []
i = 0
j = 0
my_list_1 = my_list.copy()

while j != len(my_list):
    if i < 1:
        my_list_2 = my_list_1[0:2]
        my_list_2.reverse()
        i += 1
        j += 1
        result.extend(my_list_2)
    else:
        i = 0
        j += 1
        my_list_1.pop(0)
        my_list_1.pop(0)
print(result)

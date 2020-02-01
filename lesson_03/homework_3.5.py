# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
#
string_number = '0'
result = []
result_with_q = []
my_sum = 0
my_sum2 = 0
my_sum3 = 0
while string_number.find('Q') == -1:
    string_number = input('Введите числа через пробел: ')
    if string_number.find('Q') == -1:
        my_list = string_number.split()
        numbers = []
        for i in my_list:
            number = int(i)
            numbers.append(number)
            my_sum1 = sum(numbers)
        my_sum = my_sum1 + my_sum2
        print(my_sum)
        my_sum2 = my_sum
    else:
        my_list_q = string_number.split()
        print(my_list_q)
        for i in my_list_q:
            if i != 'Q':
                i = int(i)
                my_sum3 += i
                print(my_sum3)

my_sum = my_sum + my_sum3
print(my_sum)
print('Выход из программы')

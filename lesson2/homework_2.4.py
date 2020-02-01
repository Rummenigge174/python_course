# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите несколько слов: ')
my_list = user_string.split(' ')
i = 1
for element in my_list:
    if len(element) >= 10:
        element = element[0:10]
        print(f'{i}) {element}')
        i += 1
    else:
        print(f'{i}) {element}')
        i += 1

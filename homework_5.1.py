# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
user_str = True
with open('new_file.txt', 'w') as f_obj:
    while user_str != '':
        user_str = input()
        f_obj.write(f'{user_str}\n')



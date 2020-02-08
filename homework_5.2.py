# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

i = 0
result = []
with open('my_file.txt', 'r') as f_obj:
    for line in f_obj:
        result = line.split()
        i += 1
        print(f'В {i} строке {len(result)} слова')
    print(f'В файле {i} строчек')

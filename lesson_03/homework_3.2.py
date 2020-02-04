# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

first_name_user = 'Ivan'
second_name_user = 'Ivanov'
year_user = '1991'
city_user = 'Москва'
email_user = 'ivan@ivanov.ru'
telephone_user = '1234567890'


def user_data(first_name, second_name, year, city, email, telephone):
    result = (f'{second_name} {first_name} {year} года рождения, проживающий в городе {city}. Электронный адрес: {email}, телефон: {telephone}')
    return result


print(user_data(first_name_user,second_name_user,year_user,city_user,email_user,telephone_user))

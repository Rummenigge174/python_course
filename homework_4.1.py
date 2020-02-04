# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


stavka_user = int(input('Введите почасовую ставку: '))
count_hours_user = int(input('Введите кол-во часов: '))


def my_cash(hours, stavka, award_percent):
    award = award_percent * hours * stavka / 100
    salary = hours * stavka + award
    print(salary)


my_cash(count_hours_user, stavka_user, 30)


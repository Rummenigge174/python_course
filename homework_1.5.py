# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

person_revenue = int(input('Введите значение выручки: '))
person_costs = int(input('Введите значение издержек: '))

if person_revenue - person_costs > 0:
    print('Компания отработала с прибылью')
    rent_company = (person_revenue - person_costs) / person_revenue
    print(f'Рентабильность выручки равна: {rent_company}')
    amount_person = int(input('Введите количество сотрудников: '))
    profit_on_1_worker = (person_revenue - person_costs) / amount_person
    print(f'Прибыль на 1 сотрудника равна: {profit_on_1_worker}')
else:
    print('Компания убыточная')
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

my_dict = {'wage': 5000, 'bonus': 2000}


class Worker:
    def __init__(self, name_worker, surname_worker, position_worker):
        self.name = name_worker
        self.surname = surname_worker
        self.position = position_worker
        self._income = my_dict

    def _income(self):
        wage = my_dict['wage']
        bonus = my_dict['bonus']
        return wage, bonus


class Position(Worker):
    def get_full_name(self):
        print(self.surname, self.name)

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


my_worker = Position('Alex', 'Rubanov', 'Englishman')
print(my_worker.get_full_name())
print(my_worker.get_total_income())

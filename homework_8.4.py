# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    def __init__(self):
        pass

class Equipment:
    def __init__(self):

class Printer(Equipment):
    def __init__(self):
        self.speed = 40
class Scaner(Equipment):
    def __init__(self):
        self.format = 'A4'


class Xerox(Equipment):
    def __init__(self):
        self.coping = 'B-W'

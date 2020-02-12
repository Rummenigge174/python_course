# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class  Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Порисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Порисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Порисуем маркером')


st = Stationery(title='Рисуем')
print(st.draw())
st_1 = Pen(Stationery)
print(st_1.draw())

st_2 = Pencil(Stationery)
print(st_2.draw())

st_3 = Handle(Stationery)
print(st_3.draw())

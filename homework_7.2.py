# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class MyAbc(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suits(self):
        pass

    @abstractmethod
    def common(self):
        pass


class Clothes(MyAbc):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def prop(self):
        return self.v -1

    def coat(self):
        self.res_2 = (self.v / 6.5 + 0.5)
        return self.res_2

    def suits(self):
        self.res_2 = (2 * self.h + 0.3)
        return self.res_2

    def common(self, coat, suits):
        return coat + suits


cl = Clothes(2, 2)
print(cl.coat())
print(cl.suits())
print(cl.common(cl.coat(), cl.suits()))
print(cl.prop)

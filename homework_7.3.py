# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, amount_cell):
        self.amount_cell = amount_cell

    @staticmethod
    def make_order(count_row, cell):
        while True:
            print('*' * count_row)
            cell -= count_row
            if cell < count_row:
                print('*' * cell)
                break

    def __add__(self, other):
        return self.amount_cell + other.amount_cell

    def __sub__(self, other):
        if self.amount_cell - other.amount_cell > 0:
            return self.amount_cell - other.amount_cell
        else:
            print('Результат вычетания мееньше 0')

    def __mul__(self, other):
        return self.amount_cell * other.amount_cell

    def __truediv__(self, other):
        return self.amount_cell // other.amount_cell

c1 = Cell(17)
c2 = Cell(3)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
Cell.make_order(5, c1.amount_cell)

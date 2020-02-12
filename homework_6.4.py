
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from random import randint

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина начала движение')
    def stop(self):
        print('Машина остановилась')
    def turn(self,direction):
        if direction == 'left':
            print('Машина повернула налево')
        elif direction == 'right':
            print('Машина повернула направо')
        else:
            print('некорректно введено направление')
    def show_speed(self):
        print(f'Скорость: {self.speed} км\ч')



class TownCar(Car):
    def show_speed(self):
        speed = randint(10, 100)
        if speed > 60:
            print(f'Превышение скорости на {speed - 60} км\ч')
        else:
            print(f'Скорость: {speed} км\ч')
class SportCar(Car):
    def show_speed(self):
        speed = randint(100, 200)
        if speed > 120:
            print(f'Превышение скорости на {speed - 120} км\ч')
        else:
            print(f'Скорость: {speed} км\ч')


class WorkCar(Car):
    def show_speed(self):
        speed = randint(10, 100)
        if speed > 40:
            print(f'Превышение скорости на {speed - 40} км\ч')
        else:
            print(f'Скорость: {speed} км\ч')
            
            
class PoliceCar(Car):
    def show_speed(self):
        speed = randint(10, 100)
        if speed > 40:
            print(f'Превышение скорости на {speed - 40} км\ч')
        else:
            print(f'Скорость: {speed} км\ч')


    def red_blue_light(self, is_police):
        if is_police:
            print('Включена сирена')


my_car = Car(50, 'green', 'Cellica', False)
print(my_car.show_speed())

my_car_1 = TownCar(50, 'green', 'Cellica', False)
print(my_car_1.show_speed())

my_car_2 = WorkCar(50, 'green', 'Cellica', False)
print(my_car_2.show_speed())

my_car_3 = PoliceCar(50, 'green', 'Cellica', True)
print(my_car_3.red_blue_light(is_police=True))

print(my_car.speed)
print(my_car.name)
print(my_car.color)

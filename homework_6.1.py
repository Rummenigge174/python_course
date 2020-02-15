# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
from itertools import cycle
from random import randint
lights = {1: 'red', 2:'yellow', 3:'green'}
flag = 'green'
count = 0


class TrafficLight:
    def __init__(self):
        self.__color = ['red','yellow','green']
        self.flag = 'green'
        self.count = 0


    def running(self, change_light):

            if change_light == 'red' and self.flag == 'green':
                self.flag = 'red'
                self.count += 1
                print(f'Горит {change_light}')
                time.sleep(7)
            elif change_light == 'yellow' and self.flag == 'red':
                self.flag = 'yellow'
                self.count += 1
                print(f'Горит {change_light}')
                time.sleep(2)
            elif change_light == 'green' and self.flag == 'yellow':
                self.flag = 'green'
                self.count += 1
                print(f'Горит {change_light}')
                time.sleep(10)
            else:
                print('Нарушена последовательность')


tl = TrafficLight()
while count !=10:
    i = randint(1, 3)
    # for i in range(1,4):
    rand_light = lights[i]
    print(i)
    print(rand_light)
    tl.running(rand_light)
    count += 1

